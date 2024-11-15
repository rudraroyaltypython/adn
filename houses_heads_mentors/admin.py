from django.contrib import admin
from houses_heads_mentors.models import HousesHeadsMentors

class HousesHeadsMentorsAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(HousesHeadsMentors,HousesHeadsMentorsAdmin)

# Register your models here.

