import datetime
from django.db import models
from django.contrib.auth.models import User


LANG_CHOICES = [
    ("py", "python"), # py - значение в базе данных, python - отображаемое значение
    ("cpp", "C++"),
    ("js", "JavaScript"),
]


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANG_CHOICES)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(default=datetime.datetime.now()) # auto_now=True
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    public = models.BooleanField(default=True, null=False)


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, blank=True, null=True)