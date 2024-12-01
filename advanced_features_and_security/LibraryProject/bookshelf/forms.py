from django import forms
from .models import Book  #Ensure you have the correct model imported

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Ensure this matches your model name
        fields = ['title', 'author', 'publication_year']  # Adjust fields as necessary

class ExampleForm(forms.Form):
    # Define fields for the form
    name = forms.CharField(max_length=100, label='Your Name', required=True)
    email = forms.EmailField(label='Your Email', required=True)
    message = forms.CharField(widget=forms.Textarea, label='Message', required=True)

    # Optional: You can add custom validation methods if needed
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from the domain 'example.com'")
        return email
