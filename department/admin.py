from django.contrib import admin
from .models import Department, Staff

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')
    search_fields = ('name', 'tagline')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'designation')
