from django.contrib import admin
from history.models import History

class HistoryAdmin(admin.ModelAdmin):
    list_display=['year','history']

# Register your models here.
admin.site.register(History,HistoryAdmin)
