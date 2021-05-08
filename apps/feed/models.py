from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tweet(models.Model):
    body = models.CharField(max_length=120)
    created_by = models.ForeignKey(User, related_name='tweets', on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta: 
        ordering = ('-created_at', )