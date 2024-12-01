from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book  # Import the Book model
from django.db.models import Q
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'book_list.html', {'books': books})

# View to add a new book
@login_required  # Ensure the user is logged in
@permission_required('app.can_create', raise_exception=True)  # Check if the user has permission to create books
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')

        form = BookForm(request.POST)
        if form.is_valid():  # Validates data and prevents SQL injection
            form.save()  # Safe way to save data to the database
            return redirect('book_list')
    else:
        form = BookForm()
    
    if title and author and publication_year:  # Basic validation
            Book.objects.create(title=title, author=author, publication_year=publication_year)
            return redirect('book_list')  # Redirect to the book list after saving

    return render(request, 'add_book.html')
    

# View to edit an existing book
@login_required
@permission_required('app.can_edit', raise_exception=True)  # Check if the user has permission to edit books
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')

        if title and author and publication_year:  # Basic validation
            book.title = title
            book.author = author
            book.publication_year = publication_year
            book.save()
            return redirect('book_list')

    return render(request, 'edit_book.html', {'book': book})

# View to delete a book
@login_required
@permission_required('app.can_delete', raise_exception=True)  # Check if the user has permission to delete books
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'confirm_delete.html', {'book': book})

# View to view details of a specific book

def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})


def search_books(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

