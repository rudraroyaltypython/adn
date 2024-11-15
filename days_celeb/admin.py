from django.contrib import admin
from days_celeb.models import DaysCelebration

class DaysCelebrationAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(DaysCelebration,DaysCelebrationAdmin)

# Register your models here.

