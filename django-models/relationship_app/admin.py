from django.contrib import admin
from .models import Book, UserProfile,  Library, Librarian

# Customizing the UserProfile admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Display user and role in the list view
    search_fields = ('user__username',)  # Enable search by username
    list_filter = ('role',)  # Filter by role

# Customizing the Book admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Display title and author in the list view
    search_fields = ('title', 'author')  # Enable search by title and author
    ordering = ('title',)  # Order by title

# Customizing the Library admin
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name of the library in the list view
    search_fields = ('name',)  # Enable search by library name
    filter_horizontal = ('books',)  # Use a horizontal filter for many-to-many relations

# Customizing the Librarian admin
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')  # Display librarian name and associated library
    search_fields = ('name',)  # Enable search by librarian name
    list_filter = ('library',)  # Filter by library

# Registering the models with their respective admin classes
admin.site.register(Library, LibraryAdmin)
admin.site.register(Librarian, LibrarianAdmin)

# Registering the models with their respective admin classes
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Book, BookAdmin)

# Optional: Customizing the admin site header and title
admin.site.site_header = "Library Management Admin"
admin.site.site_title = "Library Admin"
admin.site.index_title = "Welcome to Library Admin"

