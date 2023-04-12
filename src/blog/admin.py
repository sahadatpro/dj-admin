from django.contrib import admin
from blog.models import Post, Category, Profile
from django import forms
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User

class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    site_title = "Blog By Sahadat"
    index_title = "Dj Blog"
    login_template = "blog/admin/login.html"


blog_admin = BlogAdminArea(name="BlogAdmin")

blog_admin.register(User)
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

class EmailFilter(admin.SimpleListFilter):
    title = "Email Filter"
    parameter_name = "user_email" 

    def lookups(self,request, model_admin):
        return (
            ('has_email', 'Has Email'),
            ('no_email', 'No Email')
        )
    
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'has_email':
            return queryset.exclude(user__email="")
        if self.value().lower() == 'no_email':
            return queryset.filter(user__email='')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_active', 'role', 'created']
    list_filter = ['role', 'created', 'is_active', EmailFilter]

blog_admin.register(Profile, ProfileAdmin)