# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from bookshelf.forms import BookForm
from bookshelf.forms import ExampleForm



def register(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            user = form.save()  # Make sure to call save() to create the user
            auth_login(request, user)  # Log in the user after registration
            return redirect('some_view_name')  # Redirect to a success page
    else:
        form = BookForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For example, save to database or send an email
            return redirect('success_url')  # Redirect after successful submission
    else:
        form = ExampleForm()  # Create an empty form instance

    return render(request, 'bookshelf/example_template.html', {'form': form})


 # Ensure this imports correctly
def home(request):
    return render(request, 'login.html')  # Replace with your template
