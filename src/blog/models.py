from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)
    excerpt = models.TextField(null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    publish = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True)
    status = models.CharField(max_length=20, choices=STATUS, default="draft")

    def __str__(self) -> str:
        return self.title    



class Profile(models.Model):
    ROLE_OPTION = (
        ('author', 'Author'),
        ('publisher', 'Publisher'),
        ('reader', 'Reader'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    dob = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_OPTION, default='reader')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def email(self):
        return f"{self.user.email}"
    
    def __str__(self) -> str:
        return self.user.username
    