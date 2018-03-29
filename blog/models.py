from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextAreaField(max_length=5000)
    created_at = models.DateTimeField(add_now_time=True)
    updated = models.DateTimeField(add_now=True)
    created_by = models.ForeignKey(User, related_name='articles')

    def __str__(self):
        return self.title
