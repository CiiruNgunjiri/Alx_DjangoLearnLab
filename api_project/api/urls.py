from django.urls import path, include
from .views import BookViewSet, BookList
from rest_framework.routers import  DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes registered with the router
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]

