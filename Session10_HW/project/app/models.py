from tkinter import CASCADE
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # 외래키를 작성할 때 필수적으로 포함되어야할 매개변수는 참조할 테이블, 개체 관계에 사용할 이름, 개체 삭제시 수행할 동작 등 입니다.
    content = models.TextField()

    def __str__(self):
        return self.content