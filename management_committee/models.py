from django.db import models

class GoverningBody(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Department name (e.g., Urdu, English, Maths)  # Timestamp for record creation
    tagline = models.CharField(max_length=255, blank=True, null=True) 
    
    def __str__(self):
        return self.name
 
 

class CommitteeMembers(models.Model):
    name = models.CharField(max_length=100)  # Staff member's name
    designation = models.CharField(max_length=100)  # Staff designation (e.g., Professor, Assistant Teacher)
    department = models.ForeignKey(GoverningBody, on_delete=models.CASCADE, related_name='staff')  # Relates staff to a department
    achievement = models.TextField(null=True, blank=True)  # Optional achievements

    def __str__(self):
        return f"{self.name} ({self.designation})"
  