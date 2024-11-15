from django.contrib import admin
from hajwani.models import Hajwani

class HajwaniAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(Hajwani,HajwaniAdmin)

# Register your models here.

# Register your models here.
