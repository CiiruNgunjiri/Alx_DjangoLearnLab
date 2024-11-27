from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Home page to list all books
    path('add/', views.add_book, name='add_book'),  # URL to add a new book
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),  # URL to edit an existing book
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),  # URL to delete a book
    path('view/<int:book_id>/', views.view_book, name='view_book'),  # URL to view details of a specific book
]   
