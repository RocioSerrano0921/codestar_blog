from . import views  # Import views from the current directory
from django.urls import path  # Import path function from django.urls

urlpatterns = [
    path("", views.about_me, name="about"),  # Map the root URL to about view
]