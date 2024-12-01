from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class BookListView(generics.ListCreateAPIView):
    """
    View to list all books and create a new book.
    - GET /books/ : Returns a list of all books.
    - POST /books/ : Creates a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #allow read-only access for unauthenticated users
  
    def perform_create(self, serializer):
        # Custom logic before saving a new book
        serializer.save()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a book by ID.
     - GET /books/<id>/ : Retrieves a specific book by ID.
    - PUT /books/<id>/ : Updates a specific book by ID.
    - DELETE /books/<id>/ : Deletes a specific book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] #Restrict access to authenticated users only

