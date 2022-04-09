from asyncio.windows_events import NULL
from pickle import FALSE, TRUE
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100, default="")
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title