from django.contrib import admin
from dept_wise_comp.models import DepartmentWiseCompetitions

class DepartmentWiseCompetitionsAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(DepartmentWiseCompetitions,DepartmentWiseCompetitionsAdmin)

# Register your models here.