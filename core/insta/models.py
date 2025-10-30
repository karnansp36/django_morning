from django.db import models

# Create your models here.
class Insta_sign(models.Model):
    email = models.EmailField(unique=True)
    password =models.CharField()
    