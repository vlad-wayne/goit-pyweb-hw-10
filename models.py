from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.DateField(null=True, blank=True)
    born_location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    text = models.TextField()
    tags = models.JSONField()  # Список тегов
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text
