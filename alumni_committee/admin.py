from django.contrib import admin
from alumni_committee.models import Alumni_Committee

class Alumni_CommitteeAdmin(admin.ModelAdmin):
 list_display=['batch_year','name','designation','achievement','photo']


admin.site.register(Alumni_Committee,Alumni_CommitteeAdmin)

# Register your models here. 