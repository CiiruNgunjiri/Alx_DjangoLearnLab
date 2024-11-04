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

from bookshelf.models import Book
>>> #create a book instance
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> try:
...     book.save()
...     print('New book instance created successfully')
... except Exception as e:
...     print(f"An error occurred while saving the book:{e}")
... 
New book instance created successfully

#retrieve all books and display their attributes
>>> book = Book.objects.get(title="1984")
>>> print(book.title, book.author, book.publication_year)
1984 George Orwell 1949

# Update the title of the created book
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)  # Verify the update

# Delete the book instance
book = Book.objects.get(title = "Nineteen Eighty-Four")
try:
    book.delete()
    print(f"The book '{book.title}' was successfully deleted.")
except Exception as e:
    print(f"Unable to delete book: {book.title}")

# Confirm deletion by trying to retrieve all books again
books_after_deletion = Book.objects.all()
for b in books_after_deletion:
    print(b.title)

    
# Expected Output:
#The book "Nineteen Eighty-Four" was successfully deleted.

# Queryset[]

