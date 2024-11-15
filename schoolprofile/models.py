from django.db import models

class SchoolProfile(models.Model):
    school_profile=models.CharField(max_length=100)
    details=models.TextField()

# Create your models here.
