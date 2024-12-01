from django.urls import path
from .views import BookListView, BookDetailView
from .views import BookCreateView, BookUpdateView, BookDeleteView
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List and Create
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve, Update, Delete
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/update/<int:book_id>/', BookUpdateView.as_view(), name='book-update'),  # Update an existing book
    path('books/delete/<int:book_id>/', BookDeleteView.as_view(), name='book-delete'),  # Delete a specific book
]
