from django.contrib import admin
from committees_PTA_SMC.models import Committees
from committees_PTA_SMC.models import Pta
from committees_PTA_SMC.models import Others


class CommitteesAdmin(admin.ModelAdmin):
    list_display=['title','comm_description']

class PtaAdmin(admin.ModelAdmin):
    list_display=['title','PTA_description']

class OthersAdmin(admin.ModelAdmin):
    list_display=['title','others_description']

admin.site.register(Committees,CommitteesAdmin)
admin.site.register(Pta,PtaAdmin)
admin.site.register(Others)

# Register your models here.
