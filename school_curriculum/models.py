from django.db import models
from tinymce.models import HTMLField

class SchoolCurri(models.Model):
    school_curriculum_description=HTMLField()

class Divisions(models.Model):
        std=models.CharField(max_length=300)
        group=models.CharField(max_length=50)
        divisions_description=HTMLField()  

# Create your models here.
