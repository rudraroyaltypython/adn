from django.contrib import admin
from president_message.models import President

class President_Message_Admin(admin.ModelAdmin):
    list_display=['president_message','president_img']


admin.site.register(President,President_Message_Admin)
# Register your models here.    
