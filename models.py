from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)


    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self): # для Update post
        return reverse('home')

    def success_url(self):      # для Delete post
        return reverse('home')
