from django.contrib import admin
from umang.models import Umang

class UmangAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(Umang,UmangAdmin)

# Register your models here.
