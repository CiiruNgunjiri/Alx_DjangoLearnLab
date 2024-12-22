from django.urls import path
from .views import register_view, login_view, logout_view, profile_view, home_view
from .views import PostListView, PostDetailView, PostEditView, PostCreateView, PostUpdateView, PostDeleteView, BlogIndexView
from . import views
from .views import CommentCreate, CommentUpdate, CommentDelete


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('base/', home_view, name='base'),   
    path('posts/', PostListView.as_view(), name='post_list'), #List all posts
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'), #URL for viewing post details
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'), #URL for updating a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'), #URL for deleting a post
    path('posts/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('', BlogIndexView.as_view(), name='blog_index'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),  # URL for creating a post
    path('', views.index, name='blog/index'),
    path("post/new/", views.post_create, name="post_create"),  # URL for creating a new post
#    path("post/<int:pk>/update/", views.PostUpdateView, name="post_update"),  # URL for updating a post
#   path("post/<int:pk>/delete/", views.PostDeleteView, name="post_delete"),  # URL for deleting a post
    path('posts/<int:post_id>/comments/new/', CommentCreate.as_view(), name='comment_new'),
    path('comments/<int:pk>/edit/', CommentUpdate.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),
]
