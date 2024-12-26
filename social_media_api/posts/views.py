from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import FilterSet
from accounts.models import CustomUser #to access following relationships

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user #get the current user
        # Get posts from users that the current user follows
        following_users = current_user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at') # Filter posts by authors in following_users and order by creation date

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['exact', 'icontains'],
            'content': ['icontains'],
            # Add more fields as necessary for filtering.
        }

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

