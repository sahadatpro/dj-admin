from django.contrib import admin
from blog.models import Post, Category
from django import forms
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment 

class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    site_title = "Blog By Sahadat"
    index_title = "Dj Blog"
    login_template = "blog/admin/login.html"


blog_admin = BlogAdminArea(name="BlogAdmin")


blog_admin.register(Category)

class PostAdminForm(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude = ['']
    

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"

class PostAdmin(SummerAdmin):
    list_display = ['title', 'status', 'publish', 'created']

    # form = PostAdminForm
    # exclude = ['']

    fieldsets = (
        ('Basic Section', {
        'fields': ('title', 'slug', 'category')
        }),
        ('Explaination', {
        'fields': ('excerpt', 'description'),
        # 'classes': ('wide', 'extrapretty')
        }),
        ('Controlling Section', {
        'fields': ('author', 'status'),
        'classes': ('collapse', )
        })
    )

blog_admin.empty_value_display = "(None)"

blog_admin.register(Post, PostAdmin)