from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test 
from django.contrib.auth.decorators import permission_required
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library, UserProfile

def library_detail(request, library_id):
    # Fetch the library object based on the provided ID
    library = get_object_or_404(Library, id=library_id)
    return render(request, 'relationship_app/library_detail.html', {'library': library})

def library_view(request):
    return render(request, 'library.html')  

def librarian_view(request):
    return render(request, 'librarian.html')  

def member_view(request):
    return render(request, 'member.html')  


def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Specify the template to use
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
    return render(request, 'relationship_app/admin.html') 

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


