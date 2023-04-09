from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published = models.BooleanField(default=True)
    publish = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title    