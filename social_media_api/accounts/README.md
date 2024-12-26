 f
### Social Media API

### Overview
The Social Media API is a Django-based RESTful API designed to handle user authentication and management for a social media platform. This API supports user registration, login, and profile management, along with integration for social media logins via Facebook and Google.

### Table of Contents

    1. Technologies Used
    2. Setup Process
    3. User Registration and Authentication
    4. User Model Overview
    5. API Endpoints
    6. Testing the API
    7. License

### Technologies Used

    Django: A high-level Python web framework for building web applications.
    Django REST Framework: A powerful toolkit for building Web APIs in Django.
    Django Authtoken: For token-based authentication.
    Postman: For testing API endpoints.

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
To register a new user via the HTML interface, navigate to /accounts/register/ and fill out the registration form. To register a new user via the API, send a POST request to /accounts/api/register/ with the following JSON payload:

json
{
    "username": "your_username",
    "email": "your_email@example.com",
    "password": "your_password"
}

Upon successful registration, a new user will be created in the database, and an authentication token will be generated.
User Login
To log in via the HTML interface, navigate to /accounts/login/ and fill out the login form. To log in via the API, send a POST request to /accounts/api/login/ with the following JSON payload:

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
    phone_number: User's phone number (optional).
    designation: User's designation or title (optional).

Example User Model Code

python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    phone_number = models.CharField(max_length=15, blank=True)  # Optional field
    designation = models.CharField(max_length=100, blank=True)   # Optional field

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return self.username  # or f"{self.username} ({self.designation})"

API Endpoints
Method	Endpoint	Description
POST	/accounts/api/register/	Register a new user (API)
POST	/accounts/api/login/	Log in an existing user (API)
GET	/accounts/profile/	Retrieve user profile (HTML page)
GET	/accounts/register/	Render registration form (HTML)
GET	/accounts/login/	Render login form (HTML)
Testing the API
You can test the API endpoints using Postman or any other API testing tool. Make sure to set the appropriate headers for authentication when accessing protected routes.

    Register a User:
        Use POST method on /accounts/api/register/.
    Log In:
        Use POST method on /accounts/api/login/.
    Access Profile:
        Use GET method on /accounts/profile/ with appropriate authentication if required.

License
This project is licensed under the MIT License - see the LICENSE file for details. Feel free to modify this README file according to your project's specifics and add any additional information that may be relevant to users or developers interacting with your API.