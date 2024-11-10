from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test, permission_required
from .models import Book, Library, UserProfile


def library_view(request):
    return render(request, 'library.html')  # Make sure you have this template

def librarian_view(request):
    return render(request, 'librarian.html')  # Make sure you have this template

def member_view(request):
    return render(request, 'member.html')  # Make sure you have this template


def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'list_books.html', {'books': books})  # Render the template with book data

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Specify the template to use
    context_object_name = 'library'  # Name of the context variable to be used in the template

    def get_queryset(self):
        return Library.objects.prefetch_related('books')  # Optimize book retrieval



# Custom Registration View using CreateView
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('list_books')  # Redirect to list_books after successful registration

    def form_valid(self, form):
        user = form.save()  # Save the new user
        login(self.request, user)  # Log the user in immediately after registration
        return super().form_valid(form)

# Custom Login View using Django's built-in LoginView
class UserLoginView(LoginView):
    template_name = 'login.html'  # Specify the template to use

# Custom Logout View using Django's built-in LogoutView
class UserLogoutView(LogoutView):
    template_name = 'logout.html'  # Specify the template to use after logout


# Function to check if user is admin
def is_admin(user):
    return user.profile.role == 'Admin'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Function to check if user is librarian
def is_librarian(user):
    return user.profile.role == 'Librarian'

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Function to check if user is member
def is_member(user):
    return user.profile.role == 'Member'

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('list_books')  # Redirect to the list of books after adding
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('list_books')  # Redirect to the list of books after editing
    return render(request, 'edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')  # Redirect to the list of books after deletion
    return render(request, 'delete_book.html', {'book': book})
