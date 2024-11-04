```python
from bookshelf.models import Book

# Update the title of the created book

book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)  # Verify the update

# Expected Output:
'''The title of the book was updated to "Nineteen Eighty-Four".
# Nineteen Eighty-Four
