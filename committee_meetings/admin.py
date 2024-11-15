from django.contrib import admin
from committee_meetings.models import CommitteeMeetings

class CommitteeMeetingsAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(CommitteeMeetings,CommitteeMeetingsAdmin)

# Register your models here.
