from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Library
from .models import Book

# Create your views here.
# ----- Role Check Functions -----
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'
@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

class RegisterView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

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
    