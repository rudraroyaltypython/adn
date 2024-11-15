from django.contrib import admin
from home_slider.models import HomeSlider
from home_slider.models import HomeBlog

class HomeSliderAdmin(admin.ModelAdmin):
    list_display=['image1','image2','image3']


class HomeBlogAdmin(admin.ModelAdmin):
    list_display=['main_title','text_content','image1']


admin.site.register(HomeSlider,HomeSliderAdmin)
admin.site.register(HomeBlog,HomeBlogAdmin)
# Register your models here.

