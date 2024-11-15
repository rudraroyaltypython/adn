from django.contrib import admin
from admission_process.models import AdmissionProcess

class AdmissionProcessAdmin(admin.ModelAdmin):
    list_display=['main_title','text_content']


admin.site.register(AdmissionProcess,AdmissionProcessAdmin)

# Register your models here.