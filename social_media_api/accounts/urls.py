from django.urls import path
from .views import RegisterView, LoginView, ProfileView, RegisterAPIView, LoginAPIView, ListFollowersView, ListFollowingView
from .views import FollowUserView, UnfollowUserView, UserListView

urlpatterns = [
    # HTML views
    path('register/', RegisterView.as_view(), name='register'),  # View for registration (HTML form)
    path('login/', LoginView.as_view(), name='login'),          # View for login (HTML form)
    path('profile/', ProfileView.as_view(), name='profile'),     # View for user profile (HTML page)

    # API views
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),  # API view for registration
    path('api/login/', LoginAPIView.as_view(), name='api_login'),          # API view for login

    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('followers/', ListFollowersView.as_view(), name='list_followers'),  # New endpoint to list followers
    path('following/', ListFollowingView.as_view(), name='list_following'),  # New endpoint to list following users
    path('users/', UserListView.as_view(), name='user_list'),  # New endpoint to list all users
]
