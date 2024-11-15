from django.db import models
from tinymce.models import HTMLField


class Headmaster(models.Model):
    principal_image=models.FileField(upload_to="principal_image/",max_length=250,null=True,default=None)
    principal_message=HTMLField()
# Create your models here.
