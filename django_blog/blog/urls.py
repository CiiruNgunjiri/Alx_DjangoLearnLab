from django.urls import path
from .views import register_view, login_view, logout_view, profile_view, home_view
from .views import PostListView, PostDetailView, PostEditView, PostCreateView, PostUpdateView, PostDeleteView, BlogIndexView
from . import views


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('base/', home_view, name='base'),   
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('', BlogIndexView.as_view(), name='blog_index'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),  # URL for creating a post
    path('', views.index, name='blog/index'),
     path("post/new/", views.post_create, name="post-create"),  # URL for creating a new post
    path("post/<int:pk>/update/", views.post_update, name="post-update"),  # URL for updating a post
    path("post/<int:pk>/delete/", views.post_delete, name="post-delete"),  # URL for deleting a post
]
