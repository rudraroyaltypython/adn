from django.contrib import admin
from .models import GoverningBody,CommitteeMembers

@admin.register(GoverningBody)
class GoverningBodyAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')
    search_fields = ('name', 'tagline')


@admin.register(CommitteeMembers)
class CommitteeMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'designation')