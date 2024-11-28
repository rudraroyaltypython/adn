from django.contrib import admin
from .models import Committee,Members

@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')
    search_fields = ('name', 'tagline')


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'designation')
 