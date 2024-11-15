from django.db import models

# Create your models here.
class AlumniRegFormData(models.Model):
    first_name=models.CharField(max_length=50,verbose_name='First Name')
    father_or_husband_name=models.CharField(max_length=50,verbose_name='Father/Husband Name')
    surname=models.CharField(max_length=50,verbose_name='Last Name')
    address=models.CharField(max_length=500,verbose_name='Address')
    taluka=models.CharField(max_length=50,verbose_name='Taluka')
    district=models.CharField(max_length=50,verbose_name='District')
    state=models.CharField(max_length=50,verbose_name='State')
    country=models.CharField(max_length=50,verbose_name='Country')
    mobile_no=models.CharField(max_length=50,verbose_name='Mobile No (Whatsapp No)')
    email_id=models.CharField(max_length=50,verbose_name='Email')
    passed_out_from_class=models.CharField(max_length=50,verbose_name='Passed Out from the class')
    year_of_passing_out=models.CharField(max_length=50,verbose_name='Year of Passing Out')
    present_qualification=models.CharField(max_length=50,verbose_name='Present Qualification')
    present_designation=models.CharField(max_length=150,verbose_name='Present Designation')

