from django.contrib import admin
from headmaster_message.models import Headmaster

class HeadmasterAdmin(admin.ModelAdmin):
    list_display=['principal_image','principal_message']


admin.site.register(Headmaster,HeadmasterAdmin)


# Register your models here.
