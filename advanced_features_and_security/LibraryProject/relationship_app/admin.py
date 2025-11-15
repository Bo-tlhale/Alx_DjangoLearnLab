from django.contrib import admin
from .models import CustomUser

# Register your models here.
class ModelAdmin(admin.ModelAdmin):
    list_filter = ('date_of_birth', 'profile_photo')
    search_fields = ('date_of_birth', 'profile_photo')

admin.site.register(CustomUser, ModelAdmin)