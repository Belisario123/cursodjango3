from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)