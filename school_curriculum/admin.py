from django.contrib import admin
from school_curriculum.models import SchoolCurri
from school_curriculum.models import Divisions

class School_curriculumAdmin(admin.ModelAdmin):
    list_display=['school_curriculum_description']


class DiviAdmin(admin.ModelAdmin):
    list_display=['std','group','divisions_description']

admin.site.register(SchoolCurri,School_curriculumAdmin)
admin.site.register(Divisions,DiviAdmin)
# Register your models here.
