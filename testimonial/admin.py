from django.contrib import admin
from testimonial.models import Testimonial
from testimonial.models import TestimonialData


class TestimonialAdmin(admin.ModelAdmin):
    list_display=['main_title','name','user_description','photo']

class TestimonialDataAdmin(admin.ModelAdmin):
    list_display=['name','email','feedback']

# Register your models here.

admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(TestimonialData,TestimonialDataAdmin)
