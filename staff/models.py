from django.db import models


class TeachingStaff(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=100)


class NonTechingStaff(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=100)
    
# Create your models here.
