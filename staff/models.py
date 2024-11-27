from django.db import models
from tinymce.models import HTMLField



class TeachingStaff(models.Model):
    name = models.CharField(max_length=150,null=True, blank=True)
    designation = models.CharField(max_length=100,null=True, blank=True)
    achievement = HTMLField(blank=True, null=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)  # Make image optional

class NonTechingStaff(models.Model):
    name = models.CharField(max_length=150,null=True, blank=True)
    designation = models.CharField(max_length=100,null=True, blank=True)
    achievement = HTMLField(blank=True,default="No achievements yet")
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)  # Make image optional



    
# Create your models here.
 