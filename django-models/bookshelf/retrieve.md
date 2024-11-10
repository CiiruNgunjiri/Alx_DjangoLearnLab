```python
from bookshelf.models import Book

# Retrieve all books and display their attributes

book = Book.objects.get(title="1984")  # Get the book instance
print(book.title, book.author, book.publication_year)

# Expected Output:
'''Title: 1984, Author: George Orwell, Publication Year: 1949'''
# 1984 George Orwell 1949

