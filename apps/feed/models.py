from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class tweet(models.Model):
    body = models.CharField(max_length=120)
    created_by = models.ForeignKey(User, related_name='tweets', on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta: 
        ordering = ('-created_at', )

class Like(models.Model): 
    tweet = models.ForeignKey(tweet, related_name = 'likes', on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, related_name='likes', on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add=True)