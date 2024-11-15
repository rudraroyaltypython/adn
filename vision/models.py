from django.db import models
from tinymce.models import HTMLField


class Vision(models.Model):
    vision = HTMLField()


class Mission(models.Model):
    mission = HTMLField()

class Values(models.Model):
    values = HTMLField()

# Create your models here.
