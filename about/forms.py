from .models import CollaborateRequest  # Import the CollaborateRequest model
from django import forms # Import forms from Django

class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest  # Specify the model to use
        fields = ("name", "email", "message")