'''from django.contrib import admin
from .models import Comm,Members

@admin.register(Comm)
class CommAdmin(admin.ModelAdmin):
    list_display = ['committee_name']
    search_fields = ['committee_name']


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'committees']
    list_filter = ['committees']
    search_fields = ['name', 'designation']
 '''