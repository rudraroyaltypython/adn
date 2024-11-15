from django.db import models
from tinymce.models import HTMLField


class HomeSlider(models.Model):
    image1 = models.ImageField(upload_to='HomeSlider/', blank=True, null=True)  # Make image optional
    image2 = models.ImageField(upload_to='HomeSlider/', blank=True, null=True)  # Make image optional
    image3 = models.ImageField(upload_to='HomeSlider/', blank=True, null=True)  # Make image optional



class HomeBlog(models.Model):
    main_title=models.CharField(max_length=100)
    text_content=HTMLField()
    image1 = models.ImageField(upload_to='HomeBlog/', blank=True, null=True)  # Make image optional