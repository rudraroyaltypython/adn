from django.contrib import admin
from school_notice.models import SchoolNotice

class SchoolNoticeAdmin(admin.ModelAdmin):
    list_display=['main_title','date','text_content']


admin.site.register(SchoolNotice,SchoolNoticeAdmin)

# Register your models here.