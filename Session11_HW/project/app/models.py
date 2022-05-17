from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    address = models.URLField(max_length=200, blank = False, default='')
    hit = models.PositiveBigIntegerField(default=0)

    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return self.content