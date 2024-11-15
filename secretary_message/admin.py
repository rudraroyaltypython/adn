from django.contrib import admin
from secretary_message.models import Secretary


class SecretaryAdmin(admin.ModelAdmin):
    list_display=['secretary_img','Secretary_msg']
# Register your models here.


admin.site.register(Secretary,SecretaryAdmin) 