from django.shortcuts import render
from django.views import generic  # Import generic views from Django
from .models import Post  # Import the Post model

# Create your views here.

class PostList(generic.ListView):
    model = Post # Specify the model to use
    queryset = Post.objects.all() # Data set to use
    template_name = "blog/index.html" # Specify the template to use
    paginate_by = 6. # Number of posts per page
