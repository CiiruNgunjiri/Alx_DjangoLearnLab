from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in list view
    list_filter = ('author', 'publication_year')            # Fields to filter by
    search_fields = ('title', 'author__name')               # Searchable fields

admin.site.register(Book, BookAdmin)
