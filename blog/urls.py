from . import views  # Import views from the current directory
from django.urls import path  # Import path function from django.urls

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),  # Map the root URL to the PostList view
]