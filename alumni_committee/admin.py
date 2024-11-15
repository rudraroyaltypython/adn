from django.contrib import admin
from alumni_committee.models import Alumni_Committee

class Alumni_CommitteeAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(Alumni_Committee,Alumni_CommitteeAdmin)

# Register your models here.