from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display author name in list view

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Display title and author in list view
    list_filter = ('author',)            # Filter by author
    search_fields = ('title',)            # Search by title

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)               # Display library name in list view
    filter_horizontal = ('books',)         # Enable multi-select for books

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')     # Display librarian name and associated library

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Librarian, LibrarianAdmin)

