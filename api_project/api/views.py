from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Queryset for retrieving all books
    serializer_class = BookSerializer  # Use the BookSerializer for serialization

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Queryset for retrieving all books
    serializer_class = BookSerializer  # Use the BookSerializer for serialization

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
