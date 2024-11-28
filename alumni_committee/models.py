from django.db import models
from tinymce.models import HTMLField

class Alumni_Committee(models.Model):
    batch_year=models.CharField(max_length=50)
    name = models.CharField(max_length=150,null=True, blank=True)
    designation = models.CharField(max_length=100,null=True, blank=True)
    achievement = HTMLField(blank=True, null=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)  # Make image optional