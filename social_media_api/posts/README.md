### Social Media API

### Overview
The Social Media API is a Django-based RESTful API designed to handle user authentication, posts, and comments for a social media platform. This API allows users to create, view, update, and delete posts and comments, facilitating engagement within the platform.

### Table of Contents

    Technologies Used
    Setup Process
    User Registration and Authentication
    Posts and Comments Features
    User Follow Functionality
    Feed Functionality
    API Endpoints
    Testing the API
    License

Technologies Used

    Django: A high-level Python web framework for building web applications.
    Django REST Framework: A powerful toolkit for building Web APIs in Django.
    Django Authtoken: For token-based authentication.
    django-filter: For filtering capabilities in API endpoints.
    Postman: For testing API endpoints.

Setup Process
Prerequisites
Ensure you have the following installed:

    Python 3.x
    pip (Python package installer)

Step 1: Clone the Repository
Clone the project repository from GitHub:

bash
git clone https://github.com/yourusername/social_media_api.git
cd social_media_api

Step 2: Install Dependencies
Install the required Python packages:

bash
pip install django djangorestframework djangorestframework-authtoken django-filter

Step 3: Create the Posts App
Create a new app called posts:

bash
python manage.py startapp posts

Step 4: Configure Models
Define the Post and Comment models in posts/models.py:

python
from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

Step 5: Run Migrations
Run the following commands to create migrations and update the database:

bash
python manage.py makemigrations posts
python manage.py migrate

Step 6: Create Serializers
Create serializers for Post and Comment in posts/serializers.py:

python
from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

Step 7: Create Views for CRUD Operations
Implement viewsets for posts and comments in posts/views.py:

python
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

Step 8: Configure URL Routing
Define URL patterns in posts/urls.py:

python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

Include this in your main project’s urls.py:

python
from django.urls import path, include

urlpatterns = [
    path('api/', include('posts.urls')),  # Include the posts app URLs
]

Step 9: Add Pagination and Filtering
Add pagination settings in settings.py:

python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

Implement filtering capabilities in your views using Django Filter. Update your PostViewSet to include filtering.
Posts and Comments Features
Users can perform the following actions with posts and comments:

    Posts:
        Create a post (authenticated users only).
        Retrieve a list of all posts.
        Update a post (only by the author).
        Delete a post (only by the author).
    Comments:
        Create a comment on a post (authenticated users only).
        Retrieve all comments for a specific post.
        Update a comment (only by the author).
        Delete a comment (only by the author).

API Endpoints
Posts Endpoints
Method	Endpoint	Description
POST	/api/posts/	Create a new post
GET	/api/posts/	List all posts
GET	/api/posts/<id>/	Retrieve a specific post
PATCH	/api/posts/<id>/	Update an existing post
DELETE	/api/posts/<id>/	Delete an existing post
Comments Endpoints
Method	Endpoint	Description
POST	/api/comments/	Create a new comment
GET	/api/comments/?post=<id>	List all comments for a specific post
GET	/api/comments/<id>/	Retrieve a specific comment
PATCH	/api/comments/<id>/	Update an existing comment
DELETE	/api/comments/<id>/	Delete an existing comment
Testing the API
You can test the API endpoints using Postman or any other API testing tool. Make sure to set appropriate headers for authentication when accessing protected routes.

    Register a User:
        Use POST method on /accounts/api/register/.
    Log In:
        Use POST method on /accounts/api/login/.
    Create a Post:
        Use POST method on /api/posts/.
    List Posts:
        Use GET method on /api/posts/.
    Create a Comment:
        Use POST method on /api/comments/.
    List Comments for a Post:
        Use GET method on /api/comments/?post=<post_id>.
Step 3: Update User Model
In your accounts/models.py, update your custom user model to include a following field:

python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    designation = models.CharField(max_length=100, blank=True)

    # Many-to-many relationship for following users
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username

Step 4: Make Migrations
Run the following commands to create migrations and update the database:

bash
python manage.py makemigrations accounts
python manage.py migrate

Step 5: Create Follow Management Views
In accounts/views.py, create views for following and unfollowing users:

python
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CustomUser

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)

Step 6: Create Feed View
In posts/views.py, create a view that generates a feed based on the posts from users that the current user follows:

python
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get posts from users that the current user follows
        followed_users = self.request.user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')

Step 7: Define URL Patterns for New Features
Update URL patterns in accounts/urls.py for follow management:

python
from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]

Update URL patterns in posts/urls.py for the feed endpoint:

python
from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]

Step 8: Testing Follow and Feed Features
Conduct thorough tests to ensure that the follow system works as intended and that the feed correctly displays posts from followed users. Use Postman or similar tools to simulate the user experience.
User Follow Functionality
Users can perform the following actions with follows:

    Follow a User:
        Endpoint: /accounts/follow/<user_id>/
        Method: POST
    Unfollow a User:
        Endpoint: /accounts/unfollow/<user_id>/
        Method: POST

Feed Functionality
Users can view their aggregated feed of posts from users they follow:

    Get Feed:
        Endpoint: /api/feed/
        Method: GET

This endpoint returns posts from users that the authenticated user follows.
API Endpoints
Follow Management Endpoints
Method	Endpoint	Description
POST	/accounts/follow/<user_id>/	Follow a user
POST	/accounts/unfollow/<user_id>/	Unfollow a user
Feed Endpoint
Method	Endpoint	Description
GET	/api/feed/	Retrieve posts from followed users
Testing the API
You can test the API endpoints using Postman or any other API testing tool. Make sure to set appropriate headers for authentication when accessing protected routes.

    Register a User:
        Use POST method on /accounts/api/register/.
    Log In:
        Use POST method on /accounts/api/login/.
    Follow a User:
        Use POST method on /accounts/follow/<user_id>/.
    Unfollow a User:
        Use POST method on /accounts/unfollow/<user_id>/.
    Get Feed:
        Use GET method on /api/feed/.

License
This project is licensed under the MIT License - see the LICENSE file for details. Feel free to modify this README file according to your project's specifics and add any additional information that may be relevant to users or developers interacting with your API.

