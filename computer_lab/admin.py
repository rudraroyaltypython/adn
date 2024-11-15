from django.contrib import admin
from computer_lab.models import ComputerLab

class ComputerLabAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(ComputerLab,ComputerLabAdmin)

# Register your models here.
