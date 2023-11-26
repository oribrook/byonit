from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    author = models.ForeignKey(to=User, on_delete=models.RESTRICT)
    created = models.DateField(default=dt.now(), blank=True)
    modified = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"<Post: {self.title} by {self.author.username}>"