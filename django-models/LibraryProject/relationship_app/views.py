from django.shortcuts import render
from .models import Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Specify your template name
    context_object_name = 'library'        # Context variable name for the template

    def get_queryset(self):
        return Library.objects.prefetch_related('books')  # Optimize book retrieval
