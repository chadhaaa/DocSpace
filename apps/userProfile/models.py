from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical= False)
    avatar = models.ImageField(upload_to='uploads/', blank = True, null = True)
User.userProfile = property(lambda u:userprofile.objects.get_or_create(user=u)[0])