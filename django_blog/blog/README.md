# User Authentication System Documentation

## Overview
This document outlines the user authentication system implemented in the Django blog project.

### Features Included:
- User Registration: Users can create an account with a username and email.
- Login/Logout: Users can log in and out securely.
- Profile Management: Users can update their email addresses.

### How to Test:
1. Navigate to `/register` to create a new account.
2. Use `/login` to log in with your credentials.
3. Access `/profile` to update your email address.

# Authentication System Testing Documentation

## Overview
This document outlines how to test the authentication system implemented in the Django blog project.

### Running Tests
To run the authentication tests, execute the following command:
```bash
python manage.py test blog.tests

Blog Post Management Documentation
Overview
This documentation outlines the features and functionalities of the blog post management system integrated into the Django blog project. Users can create, read, update, and delete blog posts, facilitating dynamic content management for authors and easy browsing for viewers.
Features

    Create Posts: Authenticated users can create new blog posts.
    Read Posts: All users can view a list of all blog posts and read individual entries.
    Update Posts: Authors can edit their own posts.
    Delete Posts: Authors can delete their own posts.

Installation

    Ensure you have Python and Django installed.
    Clone the repository or download the project files.
    Navigate to the project directory and run:

    bash
    python manage.py migrate
    python manage.py runserver

    Access the application at http://127.0.0.1:8000/.

Usage
Step 1: Accessing Blog Posts

    Navigate to /posts/ to view a list of all blog posts.
    Click on a post title to view its full content at /posts/<int:pk>/.

Step 2: Creating a New Post

    To create a new post, go to /posts/new/.
    Fill out the form with the post title and content.
    Click "Submit" to save the new post.

Step 3: Updating an Existing Post

    To edit a post, navigate to /posts/<int:pk>/edit/.
    Make your changes in the form provided.
    Submit the form to update the post.

Step 4: Deleting a Post

    To delete a post, go to /posts/<int:pk>/delete/.
    Confirm deletion when prompted.

Permissions

    Only authenticated users can create new posts.
    Only the author of a post can edit or delete it.
    List and detail views are accessible to all users, regardless of authentication status.

Code Structure
The following files have been updated to implement CRUD operations:

    views.py: Contains class-based views for handling CRUD operations.
    forms.py: Defines PostForm using Django’s ModelForm for creating and updating posts.
    models.py: Defines the Post model with fields for title, content, and author.
    urls.py: Maps URLs to corresponding views for each CRUD operation.

Testing
Ensure that all functionalities work as expected:

    Test creating, reading, updating, and deleting posts.
    Verify that only authorized users can modify their own posts.
    Check navigation links between different views for correctness.
