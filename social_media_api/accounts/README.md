Social Media API
Overview
The Social Media API is a Django-based RESTful API designed to handle user authentication and management for a social media platform. This API supports user registration, login, and profile management, along with integration for social media logins via Facebook and Google.
Table of Contents

    Technologies Used
    Setup Process
    User Registration and Authentication
    User Model Overview
    API Endpoints
    Testing the API
    License

Technologies Used

    Django: A high-level Python web framework for building web applications.
    Django REST Framework: A powerful toolkit for building Web APIs in Django.
    Django Authtoken: For token-based authentication.
    Postman: For testing API endpoints.
    Facebook SDK & Google Sign-In: For social media authentication (if implemented).

Setup Process
Prerequisites
Ensure you have the following installed:

    Python 3.x
    pip (Python package installer)

Step 1: Clone the Repository
Clone the project repository from GitHub:

bash
git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
cd social_media_api

Step 2: Install Dependencies
Install the required Python packages:

bash
pip install django djangorestframework djangorestframework-authtoken

Step 3: Configure the Project

    Database Migrations: Run migrations to set up the database:

bash
python manage.py migrate

Create a Superuser (optional for admin access):

    bash
    python manage.py createsuperuser

Step 4: Run the Development Server
Start the Django development server:

bash
python manage.py runserver

The API will be accessible at http://127.0.0.1:8000/.
User Registration and Authentication
User Registration
To register a new user, send a POST request to /api/accounts/register/ with the following JSON payload:

json
{
    "username": "your_username",
    "email": "your_email@example.com",
    "password": "your_password"
}

Upon successful registration, a new user will be created in the database.
User Login
To log in, send a POST request to /api/accounts/login/ with the following JSON payload:

json
{
    "username": "your_username",
    "password": "your_password"
}

If successful, you will receive an authentication token in response, which you can use for subsequent requests.
Token Authentication
Include the token in the Authorization header for protected routes:

text
Authorization: Token your_auth_token_here

User Model Overview
The custom user model CustomUser extends Django’s AbstractUser and includes additional fields:

    username: Unique identifier for each user.
    email: User's email address.
    bio: A short biography of the user (optional).
    profile_picture: URL to the user's profile picture (optional).
    followers: A ManyToMany field that allows users to follow each other.

Example User Model Code

python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

API Endpoints
Method	Endpoint	Description
POST	/api/accounts/register/	Register a new user
POST	/api/accounts/login/	Log in an existing user
GET	/api/accounts/profile/	Retrieve user profile (requires auth)
Testing the API
You can test the API endpoints using Postman or any other API testing tool. Make sure to set the appropriate headers for authentication when accessing protected routes.

    Register a User:
        Use POST method on /api/accounts/register/.
    Log In:
        Use POST method on /api/accounts/login/.
    Access Profile:
        Use GET method on /api/accounts/profile/ with the Authorization header set.

License
This project is licensed under the MIT License - see the LICENSE file for details. Feel free to modify this README file according to your project's specifics and add any additional information that may be relevant to users or developers interacting with your API.
Related
What are the key components to include in a README file for a social media API
How do I explain the user registration process in a clear and concise manner
What details should be included in the user model overview
How can I make the setup process easy to follow for new users
What are the best practices for documenting authentication steps
Pro
