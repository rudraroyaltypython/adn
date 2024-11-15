from django.db import models
from tinymce.models import HTMLField

class SchoolNotice(models.Model):
    main_title=models.CharField(max_length=300)
    date=models.CharField(max_length=150)
    text_content=HTMLField()
    

