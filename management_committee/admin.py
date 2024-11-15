from django.contrib import admin
from management_committee.models import ManagementCommittee
from management_committee.models import Management_c_2016_2020
from management_committee.models import Management_c_2020_onwards
from management_committee.models import SchoolCommittee


class Management_CommitteeAdmin(admin.ModelAdmin):
    list_display=['no','committee_members_upto_1994']

class Management_c_2016_2020Admin(admin.ModelAdmin):
    list_display=['names','designation']

class Management_c_2020_onwardsAdmin(admin.ModelAdmin):
    list_display=['names','designation']

class SchoolCommitteeAdmin(admin.ModelAdmin):
        list_display=['names','designation']

# Register your models here.
admin.site.register(ManagementCommittee,Management_CommitteeAdmin)
admin.site.register(Management_c_2016_2020,Management_c_2016_2020Admin)
admin.site.register(Management_c_2020_onwards,Management_c_2020_onwardsAdmin)
admin.site.register(SchoolCommittee,SchoolCommitteeAdmin)