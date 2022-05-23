from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    address = models.URLField(max_length=200, blank = False, default='')
    hit = models.PositiveBigIntegerField(default=0)
    author = models.ForeignKey(User, models.CASCADE, related_name="posts")

    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content
