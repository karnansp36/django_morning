from django.db import models

# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password =models.CharField()