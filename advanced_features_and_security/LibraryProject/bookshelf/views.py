from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.
@permission_required('bookshef.can_create', raise_exception=True)
def create_book():
    return

@permission_required('bookshef.can_edit', raise_exception=True)
def edit_book():
    return

@permission_required('bookshef.can_view', raise_exception=True)
def view_book():
    return

@permission_required('bookshef.can_delete', raise_exception=True)
def delete_book():
    return

@permission_required('bookshef.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    context = {'list_of_books': books}
    return render(request, '/book_list.html', context)