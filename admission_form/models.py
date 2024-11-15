from django.db import models

class AdmissionForm(models.Model):
    pdf = models.FileField(upload_to='AdmissionForm/',null=False,default="")
    

   
 