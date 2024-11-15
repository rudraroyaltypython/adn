from django.contrib import admin
from vision.models import Vision
from vision.models import Mission
from vision.models import Values

class VisionAdmin(admin.ModelAdmin):
    list_display=['vision']


class MissionAdmin(admin.ModelAdmin):
    list_display=['mission']


class ValuesAdmin(admin.ModelAdmin):
    list_display=['values']



admin.site.register(Vision,VisionAdmin)
admin.site.register(Mission,MissionAdmin)
admin.site.register(Values,ValuesAdmin)
# Register your models here.
