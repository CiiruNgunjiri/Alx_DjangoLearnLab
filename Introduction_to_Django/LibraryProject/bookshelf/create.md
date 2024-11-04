```python
from bookshelf.models import Book

# Create a Book instance

>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Save the book and print a confirmation message
>>> try:
...     book.save()
...     print("New book instance created successfully.")
... except Exception as e:
...     print(f"An error occurred while saving the book: {e}")


# Expected Output:
'''New book instance created successfully'''
# New book instance created successfully.