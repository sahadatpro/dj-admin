from django.contrib import admin
from blog.models import Post, Category

class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    site_title = "Blog By Sahadat"
    index_title = "Dj Blog"


blog_admin = BlogAdminArea(name="BlogAdmin")


blog_admin.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'publish', 'created']

blog_admin.empty_value_display = "(None)"

blog_admin.register(Post, PostAdmin)

