from django.shortcuts import render
from .models import About

# Create your views here.

def about_me(request):
    ''''
    Render the about page.
    '''
    about = About.objects.all().order_by('-updated_on').first()  # Get all About instances ordered by updated_on descending
    return render(
        request, 
        "about/about.html", 
        {"about": about}  # Pass the latest About instance to the template context)
    )