from django.contrib import admin
from learning_ideal_way.models import Learning_Ideal_way


class Learning_Ideal_wayAdmin(admin.ModelAdmin):
    list_display=['learning_Ideal_way']



admin.site.register(Learning_Ideal_way,Learning_Ideal_wayAdmin)
# Register your models here.
