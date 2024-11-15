from django.db import models

class SubscribeNewsletter(models.Model):
    mail=models.CharField(max_length=50)
