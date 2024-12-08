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
