from .models import Comment # Import the Comment model
from django import forms # Import forms from Django


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Specify the model to use
        fields = ("body",)  # Fields to include in the form
