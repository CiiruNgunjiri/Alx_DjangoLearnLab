# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from bookshelf.forms import BookForm
 # Ensure this imports correctly

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
