from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Library
from .models import Book

# Create your views here.
class RegisterView(CreateView):
    form_class = UserCreationForm
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
    