from django.shortcuts import render, get_object_or_404  # Import render and get_object_or_404 functions
from django.views import generic  # Import generic views from Django
from .models import Post  # Import the Post model

# Create your views here.

class PostList(generic.ListView):
    model = Post # Specify the model to use
    queryset = Post.objects.all() # Data set to use
    template_name = "blog/index.html" # Specify the template to use
    paginate_by = 6. # Number of posts per page

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )