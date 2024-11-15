from django.contrib import admin
from alumni_meet_and_events.models import AlumniMeetEvents

class AlumniMeetEventsAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(AlumniMeetEvents,AlumniMeetEventsAdmin)

# Register your models here.