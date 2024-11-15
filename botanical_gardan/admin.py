from django.contrib import admin
from botanical_gardan.models import BotanicalGarden

class BotanicalGardenAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(BotanicalGarden,BotanicalGardenAdmin)

# Register your models here.

# Register your models here.
