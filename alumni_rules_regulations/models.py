from django.db import models
from tinymce.models import HTMLField

class AlumniRules(models.Model):
    main_title=models.CharField(max_length=50)
    sub_title=models.CharField(max_length=150)
    text_content=HTMLField()