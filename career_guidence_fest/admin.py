from django.contrib import admin
from career_guidence_fest.models import CareerGuidenceFest

class CareerGuidenceFestAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(CareerGuidenceFest,CareerGuidenceFestAdmin)

# Register your models here.
