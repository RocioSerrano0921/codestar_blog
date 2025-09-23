from django.contrib import admin
from .models import About, CollaborateRequest

# import class SummernoteModelAdmin, that defines Summernote editor
from django_summernote.admin import SummernoteModelAdmin  

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)  # Use Summernote editor for the content field

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)