from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)


    def __str__(self) -> str:
        return self.name