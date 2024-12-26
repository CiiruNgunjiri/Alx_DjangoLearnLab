### Social Media API

### Overview
The Social Media API is a Django-based RESTful API designed to handle user authentication, posts, and comments for a social media platform. This API allows users to create, view, update, and delete posts and comments, facilitating engagement within the platform.

### Table of Contents

    Technologies Used
    Setup Process
    User Registration and Authentication
    Posts and Comments Features
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

License
This project is licensed under the MIT License - see the LICENSE file for details. Feel free to modify this README file according to your project's specifics and add any additional information that may be relevant to users or developers interacting with your API.