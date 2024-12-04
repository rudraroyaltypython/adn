from django.db import models
from tinymce.models import HTMLField

class ShoolCommitteeChairpersonMessage(models.Model):
    ShoolCommitteeChairpersonMessage_img=models.FileField(upload_to='ShoolCommitteeChairpersonMessage_img/',max_length=300,null=True,default=None)
    ShoolCommitteeChairpersonMessage_msg=HTMLField()

# Create your models here.
