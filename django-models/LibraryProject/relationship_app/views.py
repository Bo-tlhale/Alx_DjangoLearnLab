from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from .models import Book

# Create your views here.
def get_all_books(request):
    books = Book.objects.all()
    context = {'list_of_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailsView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context
    