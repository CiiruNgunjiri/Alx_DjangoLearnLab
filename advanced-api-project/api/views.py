from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
import json

class BookCreateView(View):
    """
    View to create a new book.
    """
    def post(self, request):
        data = json.loads(request.body)
        book_name = data.get('book_name')
        
        if book_name:
            book = Book.objects.create(book_name=book_name)
            return JsonResponse({'id': book.id, 'book_name': book.book_name}, status=201)
        return JsonResponse({'error': 'Book name is required.'}, status=400)

class BookUpdateView(View):
    """
    View to update an existing book.
    """
    def put(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        data = json.loads(request.body)
        book_name = data.get('book_name')

        if book_name:
            book.book_name = book_name
            book.save()
            return JsonResponse({'id': book.id, 'book_name': book.book_name}, status=200)
        return JsonResponse({'error': 'Book name is required.'}, status=400)

class BookDeleteView(View):
    """
    View to delete a specific book by ID.
    """
    def delete(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully.'}, status=204)

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

