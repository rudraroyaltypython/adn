from django.db import models
from tinymce.models import HTMLField

class Secretary(models.Model):
    secretary_img=models.FileField(upload_to='secretary_img/',max_length=300,null=True,default=None)
    Secretary_msg=HTMLField()

# Create your models here.
