from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Subject(models.Model):
    major = models.ForeignKey(
        "Major", related_name="subject", on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=200)
    prof_name = models.CharField(max_length=200)
    memo = models.CharField(max_length=200)

    def __str__(self):
        return self.subject_name
