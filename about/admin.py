from django.contrib import admin
from .models import About

# import class SummernoteModelAdmin, that defines Summernote editor
from django_summernote.admin import SummernoteModelAdmin  

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)  # Use Summernote editor for the content field