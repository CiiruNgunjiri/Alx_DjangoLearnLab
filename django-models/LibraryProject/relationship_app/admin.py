from django.contrib import admin
from .models import Author, Book, Library, Librarian

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author__name')

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')

# Registering models with their respective admin classes
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Librarian, LibrarianAdmin)

