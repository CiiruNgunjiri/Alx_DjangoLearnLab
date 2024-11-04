```python
from bookshelf.models import Book

# Create a Book instance

>>> book = Book(title="1984", author="George Orwell", publication_year=1949)

# Save the book and print a confirmation message
>>> try:
...     book.save()
...     print("Book instance created successfully.")
... except Exception as e:
...     print(f"An error occurred while saving the book: {e}")


# Expected Output:
'''Book instance created successfully'''
# Book instance created successfully.