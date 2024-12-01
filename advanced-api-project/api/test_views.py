from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user for testing authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', publication_year=2020, author=self.author)

    def test_create_book(self):
        """Test creating a new book"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-list')  # Adjust based on your URL configuration
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # One existing book + one new book
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_get_books(self):
        """Test retrieving the list of books"""
        url = reverse('book-list')
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book exists

    def test_update_book(self):
        """Test updating an existing book"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Book', 'publication_year': 2021, 'author': self.author.id}
        
        response = self.client.put(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-detail', args=[self.book.id])
        
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Ensure the book is deleted

    def test_filter_books(self):
        """Test filtering books by title"""
        url = reverse('book-list') + '?title=Test'
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return the test book

    def test_search_books(self):
        """Test searching books by title"""
        url = reverse('book-list') + '?search=Test'
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return the test book

    def test_order_books(self):
        """Test ordering books by title"""
        url = reverse('book-list') + '?ordering=title'
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permissions(self):
        """Test permissions for unauthenticated users"""
        url = reverse('book-list')
        
        response = self.client.post(url, {})  # Attempt to create without login
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Should be forbidden

# Testing Strategy for API Endpoints

## Overview

"""This document outlines the unit testing strategy for the API endpoints related to the Book model in the Django REST Framework application.

## Test Cases

1. **CRUD Operations**:
   - Creating a new book.
   - Retrieving the list of books.
   - Updating an existing book.
   - Deleting a book.

2. **Filtering and Searching**:
   - Filtering books by title.
   - Searching books by title.

3. **Ordering**:
   - Ordering books by title.

4. **Permissions**:
   - Ensuring that unauthenticated users cannot create or modify books.

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test api
"""

"""By following these steps and implementing these tests, you will ensure that your API behaves as expected under various conditions and inputs. This will help maintain integrity and reliability as you continue to develop your application.
"""