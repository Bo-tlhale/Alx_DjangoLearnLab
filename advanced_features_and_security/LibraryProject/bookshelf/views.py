from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
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
    return render(request, 'bookshelf/book_list.html', context)

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data safely
            cleaned_data = form.cleaned_data
            # e.g., print(cleaned_data) or save to DB
            return render(request, 'success.html')
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})