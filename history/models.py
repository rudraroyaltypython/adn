from django.db import models

class History(models.Model):
    year=models.CharField(max_length=50)
    history=models.TextField()

# Create your models here.
