from django.contrib import admin
from sports_facility.models import SportsFacilty

class SportsFaciltyAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(SportsFacilty,SportsFaciltyAdmin)

# Register your models here.

