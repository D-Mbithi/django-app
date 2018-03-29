from django.db import models
from django.conf import settings
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='articles'
            )

    def __str__(self):
        return self.title
