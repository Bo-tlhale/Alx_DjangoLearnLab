from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)