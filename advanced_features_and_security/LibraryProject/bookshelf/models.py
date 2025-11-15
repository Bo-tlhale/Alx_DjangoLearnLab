from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

#Models
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    objects = CustomUserManager()

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_create", "Can Create"),
            ("can_edit", "Can Edit"),
            ("can_view", "Can View"),
            ("can_delete", "Can Delete"),
        ]

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name != 'bookshelf':
        return
    
    admins, created = Group.objects.get_or_create(name='Admins')
    editors, created = Group.objects.get_or_create(name='Editors')
    viewers, created = Group.objects.get_or_create(name='Viewers')

    try:
        can_create = Permission.objects.get(codename='can_create')
        can_edit = Permission.objects.get(codename='can_edit')
        can_view = Permission.objects.get(codename='can_view')
        can_delete = Permission.objects.get(codename='can_delete')
    except Permission.DoesNotExist:
        return
    
    admins.permissions.set([can_create, can_edit, can_view, can_delete])
    editors.permissions.set([can_create, can_edit, can_view])
    viewers.permissions.set([can_view])

