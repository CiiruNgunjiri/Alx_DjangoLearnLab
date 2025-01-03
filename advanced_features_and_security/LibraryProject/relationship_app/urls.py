from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, RegisterView, UserLoginView, UserLogoutView
from .views import admin_view, librarian_view, member_view, add_book, edit_book, delete_book, library_detail
from .views import register

urlpatterns = [
    path('register/', views.register, name='register'),  # Correctly specify the view
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', RegisterView.as_view(), name='register'),  # Registration URL using class-based view
    path('login/', UserLoginView.as_view(), name='login'),      # Login URL using class-based view
    path('logout/', UserLogoutView.as_view(), name='logout'),    # Logout URL using class-based view
    path('admin/', admin_view, name='admin_view'),          # Admin view URL
    path('librarian/', librarian_view, name='librarian_view'),  # Librarian view URL
    path('member/', member_view, name='member_view'),      # Member view URL
    path('books/add/', add_book, name='add_book'),          # URL for adding a book
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),  # URL for editing a book
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),  # URL for deleting a book
    path('library/<int:library_id>/', library_detail, name='library_detail'),
    path('register/', register, name='register'), 
    path('login/', UserLoginView.as_view(template_name='login.html'), name='login'),  # Correctly set the login view
    path('logout/', UserLogoutView.as_view(template_name='logout.html'), name='logout'),
    path('add_book/', add_book, name='add-book'),  # URL for adding a book
    path('edit_book/<int:book_id>/', edit_book, name='edit-book'),  # URL for editing a book
    path('admin/', admin_view, name='admin-view'),          # Admin view URL
    path('librarian/', librarian_view, name='librarian-view'),  # Librarian view URL
    path('member/', member_view, name='member-view'),      # Member view URL
    path('register/', register, name='register'),  # URL for user registration
    
]
