from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment
import datetime

class AuthTests(TestCase):
    def setUp(self):
        # Define user credentials
        self.credentials = {
            'username': 'testuser',
            'password': 'testpass'
        }
        # Create a user for testing
        self.user = User.objects.create_user(**self.credentials)

    def test_login_success(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass',
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful login

    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpass',
            'password2': 'newpass',
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful registration

    def test_logout(self):
        # Log in first
        response = self.client.post(reverse('logout'))  # Ensure you're using the correct URL name
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after logout

    def test_login_failure(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Expecting to stay on login page
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_profile_update(self):
        self.client.login(**self.credentials)
        response = self.client.post(reverse('profile'), {
            'email': 'updated@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful update
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updated@example.com')

    def test_csrf_token_in_login_form(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'csrfmiddlewaretoken')

class BlogPostTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a post with the user as the author
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)

    def test_blog_category_list_view(self):
        response = self.client.get(reverse('blog:post_list'))  # Adjust URL name as needed
        self.assertEqual(response.status_code, 200)  # Expecting a 200 status code for successful response
    
    def test_blog_category_list_view(self):
        response = self.client.get(reverse('blog:post_list'))  # Adjust URL name as needed
        self.assertEqual(response.status_code, 200)  # Expecting a 200 status code for successful response

        self.post.categories.add(self.category)

    def test_blog_index_view(self):
        """Test that the blog index view returns a 200 status code."""
        response = self.client.get(reverse('app_name:blog/index'))
        self.assertEqual(response.status_code, 200)

    def test_blog_category_list_view(self):
        """Test that the post list view returns a 200 status code."""
        response = self.client.get(reverse('blog/post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        """Test that the post detail view returns a 200 status code."""
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_post_creation_by_authenticated_user(self):
        """Test that an authenticated user can create a post."""
        self.client.login(username='testuser', password='testpass')  # Log in first
        response = self.client.post(reverse('post_create'), {
            'title': 'New Post',
            'content': 'This is a new post.',
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful creation

    def test_unauthorized_user_cannot_edit_post(self):
        """Test that an unauthorized user cannot edit a post."""
        response = self.client.get(reverse('post_edit', args=[self.post.id]))
        self.assertEqual(response.status_code, 403)  # Expecting a 403 Forbidden status code for unauthorized access

    def test_unauthorized_user_cannot_delete_post(self):
        """Test that an unauthorized user cannot delete a post."""
        response = self.client.post(reverse('post_delete', args=[self.post.id]))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('post_delete', args=[self.post.id])}")

    def test_navigation_links(self):
        """Test that navigation links work correctly."""
        response = self.client.get(reverse('blog_index'))
        self.assertEqual(response.status_code, 200)

class CommentCreationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_create_comment(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('comment_new', kwargs={'post_id': self.post.id}), {'content': 'Great post!'})
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful creation
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().content, 'Great post!')

class CommentEditingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='Initial comment')

    def test_edit_comment(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('comment_edit', kwargs={'pk': self.comment.id}), {'content': 'Edited comment'})
        self.comment.refresh_from_db()  # Refresh the comment instance from the database
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful edit
        self.assertEqual(self.comment.content, 'Edited comment')

class CommentDeletionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='Comment to delete')

    def test_delete_comment(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('comment_delete', kwargs={'pk': self.comment.id}))
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful deletion
        self.assertEqual(Comment.objects.count(), 0)

class CommentPermissionTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user1)
        self.comment = Comment.objects.create(post=self.post, author=self.user1, content='User1 comment')

    def test_non_author_cannot_edit_comment(self):
        self.client.login(username='user2', password='password2')
        response = self.client.get(reverse('comment_edit', kwargs={'pk': self.comment.id}))
        self.assertEqual(response.status_code, 403)  # Forbidden access

    def test_non_author_cannot_delete_comment(self):
        self.client.login(username='user2', password='password2')
        response = self.client.post(reverse('comment_delete', kwargs={'pk': self.comment.id}))
        self.assertEqual(response.status_code, 403)  # Forbidden access
