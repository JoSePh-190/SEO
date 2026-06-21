from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)

    excerpt = models.TextField(blank=True)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title