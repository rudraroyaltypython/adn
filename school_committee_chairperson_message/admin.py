from django.contrib import admin
from school_committee_chairperson_message.models import ShoolCommitteeChairpersonMessage


class ShoolCommitteeChairpersonMessageAdmin(admin.ModelAdmin):
    list_display=['ShoolCommitteeChairpersonMessage_img','ShoolCommitteeChairpersonMessage_msg']
# Register your models here.


admin.site.register(ShoolCommitteeChairpersonMessage,ShoolCommitteeChairpersonMessageAdmin) 