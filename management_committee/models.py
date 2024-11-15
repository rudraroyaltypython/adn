from django.db import models

class ManagementCommittee(models.Model):
    no=models.CharField(max_length=50)
    committee_members_upto_1994=models.CharField(max_length=100)

class Management_c_2016_2020(models.Model):
    names=models.CharField(max_length=100)
    designation=models.CharField(max_length=50)

class Management_c_2020_onwards(models.Model):
    names=models.CharField(max_length=100)
    designation=models.CharField(max_length=50)

class SchoolCommittee(models.Model):
    names=models.CharField(max_length=100)
    designation=models.CharField(max_length=50)

# Create your models here.
