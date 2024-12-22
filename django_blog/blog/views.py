from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login')
        else:
            # Handle invalid registration
            return render(request, 'blog/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')  # Replace with your home URL name
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid credentials'})
    return render(request, 'blog/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("login") # Replace with your login URL name

@login_required
def profile_view(request):
    if request.method == 'POST':
        request.user.email = request.POST['email']
        request.user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    return render(request, 'blog/profile.html', {'user': request.user})

def home_view(request):
    return render(request, 'blog/base.html')  # Ensure you have a home.html template


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

class PostEditView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'  # Adjust the template path as necessary
    fields = ['title', 'content']  # Specify the fields you want to edit

    def get_success_url(self):
        return HttpResponseRedirect('post_list')  # Redirect after successful edit

class BlogIndexView(ListView):
    model = Post
    template_name = 'blog/index.html'  # Adjust the template path as necessary
    context_object_name = 'posts'

def post_create(request):
    # Your logic for creating a post goes here
    return render(request, 'blog/post_create.html')

def index(request):
    context = {}
    limit = 10  # Limit to the latest 10 posts

    # Fetch posts, filtering out drafts for non-superusers
    if request.user.is_superuser:
        posts = Post.objects.all()[:limit]
    else:
        posts = Post.objects.filter(is_draft=False, published_date__lte=timezone.now())[:limit]

    context['posts'] = posts
    return render(request, 'blog/index.html', context)

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        return redirect('post_detail', pk=self.object.post.pk)
