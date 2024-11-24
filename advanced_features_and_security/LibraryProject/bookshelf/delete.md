```python
from bookshelf.models import Book

# Delete the book instance
book = Book.objects.get(title = "Nineteen Eighty-Four")
try:
    book.delete()
    print(f"The book '{book.title}' was successfully deleted.")
finally:
    pass

# Confirm deletion by trying to retrieve all books again
books_after_deletion = Book.objects.all()
for b in books_after_deletion:
    print(b.title)

    
# Expected Output:
#The book "Nineteen Eighty-Four" was successfully deleted.

# Queryset[]
