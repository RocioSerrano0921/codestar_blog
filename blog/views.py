from django.shortcuts import render
from django.views import generic  # Import generic views from Django
from .models import Post  # Import the Post model

# Create your views here.

class PostList(generic.ListView):
    model = Post # Specify the model to use
    queryset = Post.objects.all() # Retrieve all Post objects
    template_name = "blog/index.html"
    paginate_by = 6
