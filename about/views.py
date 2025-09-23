from pyexpat.errors import messages
from django.shortcuts import render
from django.contrib import messages  # Import messages framework
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about_me(request):
    ''''
    Render the about page.
    '''

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()  # Save the form data to the database
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days."
            )
    
    about = About.objects.all().order_by('-updated_on').first()  # Get all About instances ordered by updated_on descending
    collaborate_form = CollaborateForm()  # Reinitialize an empty form after saving

    return render(
        request, 
        "about/about.html", 
        {
            "about": about,  # Pass the latest About instance to the template context
            "collaborate_form": collaborate_form
        },
    )
