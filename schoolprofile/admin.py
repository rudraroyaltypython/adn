from django.contrib import admin
from schoolprofile.models import SchoolProfile

class SchoolProfileAdmin(admin.ModelAdmin):
    list_display=['school_profile','details']



admin.site.register(SchoolProfile,SchoolProfileAdmin)

# Register your models here.
