from django.contrib import admin
from staff.models import TeachingStaff
from staff.models import NonTechingStaff


class TeachingStaffAdmin(admin.ModelAdmin):
    list_display=['name','designation']

class NonTeachingStaffAdmin(admin.ModelAdmin):
    list_display=['name','designation']


admin.site.register(TeachingStaff,TeachingStaffAdmin)
admin.site.register(NonTechingStaff,NonTeachingStaffAdmin)
# Register your models here.
