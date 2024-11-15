from django.db import models
from tinymce.models import HTMLField

class Committees(models.Model):
    title=models.CharField(max_length=100)
    comm_description= HTMLField()

class Pta(models.Model):
    title=models.CharField(max_length=50)
    PTA_description=HTMLField()

class Others(models.Model):
    title=models.CharField(max_length=100)
    others_description=HTMLField()

# Create your models here.
