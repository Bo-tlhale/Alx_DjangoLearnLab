from django.contrib import admin
from .models import CustomUser, Book

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ('date_of_birth', 'profile_photo')
    search_fields = ('date_of_birth', 'profile_photo')

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)