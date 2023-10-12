from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    genre = models.CharField(max_length=255, null=True)
    amount = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)