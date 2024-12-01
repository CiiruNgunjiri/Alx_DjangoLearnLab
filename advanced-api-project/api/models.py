from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Represents an author with a name.
    Each author can have multiple books associated with them.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book with a title, publication year, and an associated author.
    Each book is linked to one author, establishing a one-to-many relationship.
    """
    
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
