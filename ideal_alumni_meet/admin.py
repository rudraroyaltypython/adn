from django.contrib import admin
from ideal_alumni_meet.models import IdealAlumniMeet

class IdealAlumniMeetAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(IdealAlumniMeet,IdealAlumniMeetAdmin)

# Register your models here.
