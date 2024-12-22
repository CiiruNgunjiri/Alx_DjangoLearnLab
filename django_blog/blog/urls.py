from django.urls import path
from .views import register_view, login_view, logout_view, profile_view, home_view
from .views import PostListView, PostDetailView, PostEditView, PostCreateView, PostUpdateView, PostDeleteView, BlogIndexView
from . import views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from django.contrib.auth import views as auth_views
app_name = 'blog'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('base/', home_view, name='base'),   
    path('post/', PostListView.as_view(), name='post_list'), #List all posts
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'), #URL for viewing post details
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'), #URL for updating a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'), #URL for deleting a post
    path('posts/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('', BlogIndexView.as_view(), name='blog_index'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),  # URL for creating a post
    path('', views.index, name='blog/index'),
    path("post/new/", views.post_create, name="post_create"),  # URL for creating a new post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_new'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:login'), name='logout'),
#    path('profile/', profile_view.as_view(), name='profile'),
#    path('register/', register_view.as_view(), name='register')
#   path("post/<int:pk>/update/", views.PostUpdateView, name="post_update"),  # URL for updating a post
#   path("post/<int:pk>/delete/", views.PostDeleteView, name="post_delete"),  # URL for deleting a post
]
