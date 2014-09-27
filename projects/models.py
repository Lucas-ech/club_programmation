from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    author = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now_add=True, auto_now=True)
    language = models.ForeignKey(Language)
    source = models.URLField(blank=True)
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.content
