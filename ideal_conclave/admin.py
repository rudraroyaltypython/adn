from django.contrib import admin
from ideal_conclave.models import IdealConclave

class IdealConclaveAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content','image1','image2','image3']


admin.site.register(IdealConclave,IdealConclaveAdmin)

# Register your models here.
