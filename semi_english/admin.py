from django.contrib import admin
from semi_english.models import SemiEnglish

class SemiEnglishAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']

# Register your models here.
admin.site.register(SemiEnglish,SemiEnglishAdmin)