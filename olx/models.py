from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=250)
    image_url = models.CharField(max_length=2083, blank=True)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
