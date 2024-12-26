from django.urls import path
from .views import RegisterView, LoginView, ProfileView, RegisterAPIView, LoginAPIView

urlpatterns = [
    # HTML views
    path('register/', RegisterView.as_view(), name='register'),  # View for registration (HTML form)
    path('login/', LoginView.as_view(), name='login'),          # View for login (HTML form)
    path('profile/', ProfileView.as_view(), name='profile'),     # View for user profile (HTML page)

    # API views
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),  # API view for registration
    path('api/login/', LoginAPIView.as_view(), name='api_login'),          # API view for login
]