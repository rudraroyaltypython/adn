from django.contrib import admin
from school_parliment.models import SchoolParliment

class SchoolParlimentAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(SchoolParliment,SchoolParlimentAdmin)

# Register your models here.
