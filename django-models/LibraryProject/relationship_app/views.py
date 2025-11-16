from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test, permission_required, login_required
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Library
from .models import Book
from .models import User as user
from .models import UserProfile as userprofile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm();
            message = 'Please enter the correct credentials to register'
    else: 
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Librarian')
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Member')
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
@login_required
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')

        # Create new book
        Book.objects.create(
            title=title,
            author=author
        )
        return redirect('all_books')

    return render(request, 'books/add_book.html')


# ----- Edit Book -----
@permission_required('relationship_app.can_change_book', raise_exception=True)
@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date') or None
        book.save()
        return redirect('all_books')

    return render(request, 'books/edit_book.html', {'book': book})


# ----- Delete Book -----
@permission_required('relationship_app.can_delete_book', raise_exception=True)
@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('all_books')

    return render(request, 'books/delete_book.html', {'book': book})

def list_books(request):
    books = Book.objects.all()
    context = {'list_of_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context
