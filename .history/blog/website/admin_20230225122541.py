from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = []

admin.site.register(Post)