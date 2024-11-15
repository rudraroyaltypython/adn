from django.contrib import admin
from alumni_rules_regulations.models import AlumniRules

class AlumniRulesAdmin(admin.ModelAdmin):
    list_display=['main_title','sub_title','text_content']


admin.site.register(AlumniRules,AlumniRulesAdmin)

# Register your models here.