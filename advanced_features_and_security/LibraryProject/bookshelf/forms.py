from django import forms
from .models import Book  # Ensure you have the correct model imported

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Ensure this matches your model name
        fields = ['title', 'author', 'publication_year']  # Adjust fields as necessary
