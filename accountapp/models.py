from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    pswd1 = models.CharField(max_length=10)
    pswd2 = models.CharField(max_length=10)