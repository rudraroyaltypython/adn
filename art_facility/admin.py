from django.contrib import admin
from art_facility.models import ArtFaiclity

class ArtFacilityAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(ArtFaiclity,ArtFacilityAdmin)
