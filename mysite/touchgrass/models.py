from django.db import models


class Post(models.Model):
    def __str__(self):
        return self.username

    username = models.CharField(max_length=200)
    post = models.TextField()
    image = models.CharField(max_length=500, default='n/a')