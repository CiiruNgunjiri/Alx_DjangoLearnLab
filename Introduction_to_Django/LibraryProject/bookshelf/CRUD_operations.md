from bookshelf.models import Book

# CRUD_operations.md

## Create Operation
```python
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
try:
    book.save()
    print('Book instance created successfully')


#Expected Output
'''Book instance created successfully'''
#Book instance created successfully
