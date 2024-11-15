from django.db import models
from tinymce.models import HTMLField

class BotanicalGarden(models.Model):
    main_title=models.CharField(max_length=50)
    sub_title=models.CharField(max_length=150)
    text_content=HTMLField()
    image1 = models.ImageField(upload_to='botanical_garden/', blank=True, null=True)  # Make image optional
    image2 = models.ImageField(upload_to='botanical_garden/', blank=True, null=True)  # Make image optional
    image3 = models.ImageField(upload_to='botanical_garden/', blank=True, null=True)  # Make image optional