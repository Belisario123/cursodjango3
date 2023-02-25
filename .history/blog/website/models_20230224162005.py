from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    sub = models.CharField(max_length=30)