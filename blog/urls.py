from . import views  # Import views from the current directory
from django.urls import path  # Import path function from django.urls

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),  # Map the root URL to PostList view
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # Map URL with slug to post_detail view
     path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'), # Map URL for editing comments to comment_edit view
     path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'), # Map URL for deleting comments to comment_delete view
]