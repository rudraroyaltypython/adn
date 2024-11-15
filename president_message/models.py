from django.db import models
from tinymce.models import HTMLField


class President(models.Model):
    president_img=models.FileField(upload_to="president_Img/",max_length=300,null=True,default=None)
    president_message=HTMLField()

# Create your models here.
