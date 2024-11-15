from django.contrib import admin
from ideal_story.models import IdealStory


class IdealStoryAdmin(admin.ModelAdmin):
    list_display=['ideal_story']


admin.site.register(IdealStory,IdealStoryAdmin)

# Register your models here.
