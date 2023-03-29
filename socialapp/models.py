from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class LikeorDislike(models.Model):
    image = models.ImageField(upload_to='img/')
    like= models.ManyToManyField(User,related_name='forlike')
    dislike=models.ManyToManyField(User,related_name='fordislike')