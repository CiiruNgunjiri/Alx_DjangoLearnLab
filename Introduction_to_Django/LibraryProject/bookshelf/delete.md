```python
from bookshelf.models import Book

# Delete the book instance
book = Book.objects.get(title = "Nineteen Eighty-Four")
try:
    book.delete()
    print(f"The book '{book.title}' was successfully deleted.")
finally:
    pass
    
# Expected Output:
#The book "Nineteen Eighty-Four" was successfully deleted.

# Queryset[]
