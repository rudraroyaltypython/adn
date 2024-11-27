"""
URL configuration for adn_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adn_core import views
from django.conf import settings
from django.urls import include,path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('president/',views.president),
    path('secretary/',views.secretary),
    path('history/',views.history),
    path('management/',views.management),
    path('idealstory/',views.idealstory),
    path('headmaster/',views.headmaster),
    path('profile/',views.profile),
    path('vision/',views.vision),
    path('faculty/',views.faculty),
    path('committee/',views.committee),
    path('learning/',views.learning),
    path('schoolCurriculum/',views.schoolCurriculum),
    path('semi_english/',views.semi_english),
    path('science_lab/',views.science_lab),
    path('computer_lab/',views.computer_lab),
    path('MIHAJWANI/',views.MIHAJWANI),
    path('botani/',views.botani),
    path('art/',views.art),
    path('sports/',views.sports),
    path('school_parliment/',views.school_parliment),
    path('houses/',views.houses),
    path('days_celebration/',views.days_celebration),
    path('committee_meetings/',views.committee_meetings),
    path('dept_wise_comp/',views.dept_wise_comp),
    path('umang/',views.umang),
    path('career_guidence_fest/',views.career_guidence_fest),
    path('PARWAZ/',views.PARWAZ),
    path('IDEAL_ALUMNI_MEET/',views.IDEAL_ALUMNI_MEET),
    path('IDEAL_CONCLAVE/',views.IDEAL_CONCLAVE),
    path('admission_process/',views.admission_process),
    path('admission_form/',views.admission_form),
    path('alumni_rules/',views.alumni_rules),
    path('alumni_reg_form/',views.alumni_reg_form),
    path('alumni_reg_form_saved/',views.alumni_reg_form_data_save,name='alumni_reg_form_saved'),
    path('alumni_committee/',views.alumni_committee),
    path('alumni_meet/',views.alumni_meet),
    path('support_ideal/',views.support_ideal),
    path('contactus/',views.contactus),
    path('contactussubmit/',views.contactus_data,name='contactussubmit'),
    path('notice/',views.notice),
    path('subscribe-newsletter/',views.sub_newsletter),
    path('department/', views.department_staff_list, name='department'),
    path('admissionForm/', views.admission_form, name='admissionForm'),
    path('testimonial/',views.testimonial),
    path('testimonialSubmit/',views.testimonial_data,name='testimonialSubmit')


    
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)