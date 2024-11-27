from django.db import models
from tinymce.models import HTMLField

class Testimonial(models.Model):
    main_title=models.CharField(max_length=300)
    name=models.CharField(max_length=150)
    user_description=HTMLField()
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)  # Make image optional


class TestimonialData(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    feedback=models.TextField()


 
     