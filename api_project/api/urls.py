from django.urls import path, include
from .views import BookViewSet, BookList
from rest_framework.routers import  DefaultRouter
from . import views
from .views import CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view(), name='api-token-auth'),
    path('', include(router.urls)),  # Includes all routes registered with the router
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]

