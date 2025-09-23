
from django.shortcuts import render, get_object_or_404, reverse  # Import render and get_object_or_404 functions
from django.views import generic  # Import generic views from Django
from django.contrib import messages  # Import messages framework
from django.http import HttpResponseRedirect
from .models import Post, Comment  # Import the Post and Comment models
from .forms import CommentForm  # Import the CommentForm form

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

    queryset = Post.objects.filter(status=1)  # Only get posts with status=1 (published)
    post = get_object_or_404(queryset, slug=slug)  # Get the post with the given slug or return 404 if not found
    comments = post.comments.all().order_by('-created_on')  # Get all comments related to the post, ordered by creation date descending
    comment_count = post.comments.filter(approved=True).count()  # Count of approved comments for the post
    

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)  # Bind data from the request to the form
        if comment_form.is_valid(): # Check if the form is valid
            comment = comment_form.save(commit=False)  # Create a Comment object but don't save to the database yet
            comment.author = request.user  # Set the author of the comment to the current user
            comment.post = post  # Associate the comment with the current post
            comment.save()  # Save the comment to the database
            messages.add_message(
                request, messages.SUCCESS,
                "Your comment has been submitted and is awaiting approval."
            )

    comment_form = CommentForm()  # Initialize an empty comment form

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post, # The post to display
            "comments": comments,  # All comments related to the post
            "comment_count": comment_count,  # Count of approved comments for the post
            "comment_form": comment_form,  # Pass the empty comment form to the template
        },  # Pass the post, comments, comment count, and comment form to the template context
    )



def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))



def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
