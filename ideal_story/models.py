from django.db import models
from tinymce.models import HTMLField

class IdealStory(models.Model):
    ideal_story=HTMLField()
# Create your models here.
