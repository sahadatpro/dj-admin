from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'publish', 'created']

admin.site.empty_value_display = "(None)"

admin.site.register(Post, PostAdmin)