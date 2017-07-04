from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(default="")
    author = models.ForeignKey(to=User, default=None)
    date_created = models.DateField(default=now)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " : " + self.author.last_name + " " + self.author.first_name


class Comment(models.Model):
    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=250, default="")
    author = models.ForeignKey(to=User)
    date_created = models.DateField(default=now)
    isRemoved = models.BooleanField(default=False)
