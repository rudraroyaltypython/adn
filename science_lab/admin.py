from django.contrib import admin
from science_lab.models import ScienceLab

class ScienceLabAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(ScienceLab,ScienceLabAdmin)

# Register your models here.
