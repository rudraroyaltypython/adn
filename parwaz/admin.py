from django.contrib import admin
from parwaz.models import Parwaz

class ParwazAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(Parwaz,ParwazAdmin)

# Register your models here.

