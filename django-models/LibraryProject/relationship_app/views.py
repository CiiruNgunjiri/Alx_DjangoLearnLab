from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'list_books.html', {'books': books})  # Render the template with book data

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Specify the template to use
    context_object_name = 'library'  # Name of the context variable to be used in the template

    def get_queryset(self):
        return Library.objects.prefetch_related('books')  # Optimize book retrieval
