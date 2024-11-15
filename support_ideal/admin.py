from django.contrib import admin
from support_ideal.models import SupportIdeal

class SupportIdealAdmin(admin.ModelAdmin):
    list_display=['main_title','text_content']


admin.site.register(SupportIdeal,SupportIdealAdmin)

# Register your models here.
