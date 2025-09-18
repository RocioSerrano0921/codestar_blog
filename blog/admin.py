from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin # import class SummernoteModelAdmin, that defines 

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin

    list_display = ("title", "slug", "status", "created_on")  # Display these fields in the admin list view
    search_fields = ["title", "content"]  # Add a search box for the title field
    list_filter = ("status", "created_on")  # Add a filter sidebar for the status field
    prepopulated_fields = {"slug": ("title",)}  # Auto-fill the slug field based on the title
    summernote_fields = ("content",)  # Use Summernote editor for the content field

# Register your models here.

admin.site.register(Comment)