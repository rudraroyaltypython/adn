from django.db import models
from tinymce.models import HTMLField

class AdmissionProcess(models.Model):
    main_title=models.CharField(max_length=50)
    text_content=HTMLField()
   