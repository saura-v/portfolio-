from django.db import models

# Create your models here.

class ConatctViwe(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()