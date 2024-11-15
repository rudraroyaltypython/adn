from django.http import HttpResponse
from django.shortcuts import render
from president_message.models import President
from secretary_message.models import Secretary
from history.models import History
from management_committee.models import ManagementCommittee
from management_committee.models import Management_c_2016_2020
from management_committee.models import Management_c_2020_onwards
from management_committee.models import SchoolCommittee
from ideal_story.models import IdealStory
from headmaster_message.models import Headmaster
from schoolprofile.models import SchoolProfile
from vision.models import Vision
from vision.models import Mission
from vision.models import Values
from staff.models import TeachingStaff
from staff.models import NonTechingStaff
from committees_PTA_SMC.models import Committees
from committees_PTA_SMC.models import Pta
from committees_PTA_SMC.models import Others 
from learning_ideal_way.models import Learning_Ideal_way
from school_curriculum.models import SchoolCurri
from school_curriculum.models import Divisions
from semi_english.models import SemiEnglish
from science_lab.models import ScienceLab
from hajwani.models import Hajwani
from botanical_gardan.models import BotanicalGarden
from art_facility.models import ArtFaiclity
from sports_facility.models import SportsFacilty
from school_parliment.models import SchoolParliment
from houses_heads_mentors.models import HousesHeadsMentors
from days_celeb.models import DaysCelebration
from committee_meetings.models import CommitteeMeetings
from dept_wise_comp.models import DepartmentWiseCompetitions
from umang.models import Umang
from career_guidence_fest.models import CareerGuidenceFest
from parwaz.models import Parwaz
from ideal_alumni_meet.models import IdealAlumniMeet
from ideal_conclave.models import IdealConclave
from admission_process.models import AdmissionProcess
from alumni_rules_regulations.models import AlumniRules
from alumni_committee.models import Alumni_Committee
from alumni_meet_and_events.models import AlumniMeetEvents
from support_ideal.models import SupportIdeal
from home_slider.models import HomeSlider
from school_notice.models import SchoolNotice
from alumni_reg_form_data.models import AlumniRegFormData
from contact_us_data.models import ContactUS
from django.shortcuts import render, HttpResponse
from home_slider.models import HomeBlog
from newsletter.models import SubscribeNewsletter
from document.models import Document
from admission_form.models import AdmissionForm
from testimonial.models import Testimonial
from testimonial.models import TestimonialData
from computer_lab.models import ComputerLab

def homePage(request):
    home_slider_data=HomeSlider.objects.all()
    school_notice_data=SchoolNotice.objects.all()
    home_blog_data=HomeBlog.objects.all()


    home_slider_data_render={
        'home_slider' : home_slider_data,
        'school_notice':school_notice_data,
        'HomeBlog':home_blog_data
    }
    return render(request,'index.html',home_slider_data_render)

def president(request):
    p_msg=President.objects.all()
    p_msg_data={
        'p_msg_data':p_msg
    }
    return render(request,'president.html',p_msg_data)

def secretary(request):
    secretary_msg_data=Secretary.objects.all()
    sec_msg_data={
        'sec_msg' : secretary_msg_data
    }

    return render(request,'secretary.html',sec_msg_data)

def history(request):
    history_data=History.objects.all()

    his_data={
        'History_data_dic':history_data
    }
    return render(request,'history.html',his_data)

def management(request):
    management_c=ManagementCommittee.objects.all()
    management_c_2016_2020=Management_c_2016_2020.objects.all()
    management_c_2020_onwards=Management_c_2020_onwards.objects.all()
    schoolCommittee=SchoolCommittee.objects.all()

    management_c_data={
        'management_c_data':management_c,
        'management_c_data_2':management_c_2016_2020,
        'management_c_data_3':management_c_2020_onwards,
        'management_c_data_4':schoolCommittee,

    }
    return render(request,'management_committee.html',management_c_data)

def idealstory(request):
    idealstory_data=IdealStory.objects.all()

    ideal_story_data_render={
        'ideal_story':idealstory_data
    }
    return render(request,'idealstory.html',ideal_story_data_render)

def headmaster(request):
    headmaster_data=Headmaster.objects.all()

    headmaster_data_render={
        'headmaster_msg':headmaster_data
    }
    return render(request,'headmaster.html',headmaster_data_render)

def profile(request):
    profile_data=SchoolProfile.objects.all()

    profile_data_render={
        'school_profile':profile_data
    }
    return render(request,'profile.html',profile_data_render)

def vision(request):
    vision_data=Vision.objects.all()
    mission_data=Mission.objects.all()
    values_data=Values.objects.all()

    vision_data_render={
        'vision_1' : vision_data,
        'mission_2' : mission_data,
        'values_3' : values_data,
    }
    return render(request,'vision.html',vision_data_render)

def faculty(request):
    teaching_staff_data=TeachingStaff.objects.all()
    non_teaching_staff_data=NonTechingStaff.objects.all()

    staff_data_render = {
        'teaching' : teaching_staff_data,
        'Nteaching' : non_teaching_staff_data
    }
    return render(request,'staff.html',staff_data_render)

def committee(request):
    committees_data=Committees.objects.all()
    pta_data=Pta.objects.all()
    others_data=Others.objects.all()

    committee_data_render={
        'comm': committees_data,
        'pta' : pta_data,
        'others' : others_data 
    }
    return render(request,'comm_PTA.html',committee_data_render)

def learning(request):
    learning_ideal_way=Learning_Ideal_way.objects.all()

    learning_render={
        'learning_ideal':learning_ideal_way
    }
    return render(request,'learning_ideal_way.html',learning_render)

def schoolCurriculum(request):
    school_curri_data=SchoolCurri.objects.all()
    divi_data=Divisions.objects.all()

    school_curri_data_render={
        'school_curri': school_curri_data,
        'divi':divi_data
    }
    return render(request,'school_curriculum.html',school_curri_data_render)

def department_view(request):
    documents = Document.objects.all()
    return render(request, 'department.html', {'documents': documents})




def semi_english(request):
    semi_english_data=SemiEnglish.objects.all()

    semi_english_data_render={
        'semi_english':semi_english_data
    }
    return render(request,'SEMI-ENGLISH FACILITY.html',semi_english_data_render)

def science_lab(request):
    science_lab_data=ScienceLab.objects.all()

    science_lab_data_render={
        'science_lab':science_lab_data
    }
    return render(request,'science_lab.html',science_lab_data_render)

def computer_lab(request):
    computer_lab_data=ComputerLab.objects.all()

    computer_lab_data_render={
        'computer_lab_data':computer_lab_data
    }

    return render(request,'computer_lab.html',computer_lab_data_render)

def MIHAJWANI(request):
    hajwani_data=Hajwani.objects.all()

    hajwani_data_render={
        'hajwani':hajwani_data
    }
    return render(request,'Hajwani.html',hajwani_data_render)

def botani(request):
    botanical_garden_data=BotanicalGarden.objects.all()

    botanical_garden_data_render={
        'botanical_garden':botanical_garden_data
    }
    return render(request,'botani.html',botanical_garden_data_render)

def art(request):
    art_facility_data=ArtFaiclity.objects.all()

    art_facility_data_render={
        'art_facility':art_facility_data
    }
    return render(request,'art.html',art_facility_data_render)

def sports(request):
    sports_facility_data=SportsFacilty.objects.all()

    sports_facility_data_render={
        'sports_facility':sports_facility_data
    }
    return render(request,'sports.html',sports_facility_data_render)

def school_parliment(request):
    school_parliment_data=SchoolParliment.objects.all()

    school_parliment_data_render={
        'school_parliment':school_parliment_data
    }
    return render(request,'school_parliment.html',school_parliment_data_render)

def houses(request):
    houses_heads_mentors_data=HousesHeadsMentors.objects.all()

    houses_heads_mentors_data_render={
        'houses_heads_mentors':houses_heads_mentors_data
    }
    return render(request,'houses.html',houses_heads_mentors_data_render)

def days_celebration(request):
    days_celebration_data=DaysCelebration.objects.all()

    days_celebration_data_render={
        'days_celebration':days_celebration_data
    }
    return render(request,'days_celeb.html',days_celebration_data_render)

def committee_meetings(request):
    committee_meetings_data=CommitteeMeetings.objects.all()

    committee_meetings_data_render={
        'committee_meetings':committee_meetings_data
    }
    return render(request,'committee_meetings.html',committee_meetings_data_render)

def dept_wise_comp(request):
    dept_wise_comp_data=DepartmentWiseCompetitions.objects.all()

    dept_wise_comp_data_render={
        'dept_wise_comp_data' :dept_wise_comp_data
    }
    return render(request,'department_wise_comp.html',dept_wise_comp_data_render)

def umang(request):
    umang_data=Umang.objects.all()

    umang_data_render={
        'umang_data':umang_data
    }
    return render(request,'umang.html',umang_data_render)

def career_guidence_fest(request):
    career_guidence_fest_data=CareerGuidenceFest.objects.all()

    career_guidence_fest_data_render={
        'career_guidence_fest':career_guidence_fest_data
    }
    return render(request,'career_guidence_fest.html',career_guidence_fest_data_render)


def PARWAZ(request):
    parwaz_data=Parwaz.objects.all()

    parwaz_data_render={
        'parwaz':parwaz_data
    }
    return render(request,'PARWAZ.html',parwaz_data_render)

def IDEAL_ALUMNI_MEET(request):
    ideal_alumni_meet_data=IdealAlumniMeet.objects.all()

    ideal_alumni_meet_data_render={
        'ideal_alumni_meet':ideal_alumni_meet_data
    }
    return render(request,'IDEAL_ALUMNI_MEET.html',ideal_alumni_meet_data_render)

def IDEAL_CONCLAVE(request):
    ideal_conclave_data=IdealConclave.objects.all()

    ideal_conclave_data_render={
        'ideal_conclave':ideal_conclave_data
    }
    return render(request,'IDEAL_CONCLAVE.html',ideal_conclave_data_render)

def admission_process(request):
    admission_process_data=AdmissionProcess.objects.all()

    admission_process_data_render={
        'admission_process':admission_process_data
    }
    return render(request,'admission_process.html',admission_process_data_render)

def admission_form(request):
    admission_form = AdmissionForm.objects.all()
    
    return render(request, 'admission_form.html', {'admission_form': admission_form})
 

def alumni_rules(request):
    alumni_rules_data=AlumniRules.objects.all()

    alumni_rules_data_render={
        'alumni_rules':alumni_rules_data
    }
    return render(request,'alumni_rules.html',alumni_rules_data_render)

def alumni_reg_form(request):
   
    return render(request,'alumni_reg_form.html')

def alumni_reg_form_data_save(request):
    if request.method=='POST':
        name=request.POST.get('firstName')
        father_name=request.POST.get('fatherName')
        surname=request.POST.get('lastName')
        address=request.POST.get('Address-Buidling/House Name & Number')
        taluka=request.POST.get('Taluka')
        district=request.POST.get('District')
        state=request.POST.get('State')
        country=request.POST.get('Country')
        mobileNumber=request.POST.get('mobileNumber')
        email=request.POST.get('email')
        passoutClass=request.POST.get('passoutClass')
        passingYear=request.POST.get('passingYear')
        pQualification=request.POST.get('pQualification')
        designation=request.POST.get('designation')

        alumni_reg_data=AlumniRegFormData(first_name=name,father_or_husband_name=father_name,surname=surname,address=address,taluka=taluka,district=district,state=state,country=country,mobile_no=mobileNumber,email_id=email,passed_out_from_class=passoutClass,year_of_passing_out=passingYear,present_qualification=pQualification,present_designation=designation)
        alumni_reg_data.save()
    return render(request,'alumni_reg_form.html')

def alumni_committee(request):
    alumni_committee_data=Alumni_Committee.objects.all()

    alumni_committee_data_render={

        'alumni_committee':alumni_committee_data
    }
    return render(request,'alumni_committee.html',alumni_committee_data_render)

def alumni_meet(request):
    alumni_meet_data=AlumniMeetEvents.objects.all()

    alumni_meet_data_render={
        'alumni_meet': alumni_meet_data
    }
    return render(request,'alumni_meet.html',alumni_meet_data_render)

def support_ideal(request):
    support_ideal_data=SupportIdeal.objects.all()

    support_ideal_data_render={
        'support_ideal': support_ideal_data
    }
    return render(request,'support_ideal.html',support_ideal_data_render)

def contactus(request):
    return render(request,'contactus.html')

def contactus_data(request):
    if request.method=="POST":
        your_name=request.POST.get('name')
        your_email=request.POST.get('email')
        your_subject=request.POST.get('subject')
        your_message=request.POST.get('message')

        contact=ContactUS(name=your_name,mail=your_email,subject=your_subject,message=your_message)
        contact.save()
    
    return render(request,'contactus.html')

def sub_newsletter(request):
    if request.method=="POST":
        newsletter_mail=request.POST.get('newsletter')

        contact_mail=SubscribeNewsletter(mail=newsletter_mail)
        contact_mail.save()

    return render(request,'index.html')

def notice(request):
    notice_data=SchoolNotice.objects.all()

    notice_data_render={
        'notice': notice_data
    }
    return render(request,'notice.html',notice_data_render)

def testimonial(request):
    testimonial_data=Testimonial.objects.all()

    testimonial_data_redner={
        'testimonial_data': testimonial_data
    }

    return render(request,'testimonial.html',testimonial_data_redner)

def testimonial_data(request):
    if request.method=="POST":
        feedback_user_name=request.POST.get('name')
        feedback_user_email=request.POST.get('email')
        feedback=request.POST.get('feedback')

        feedback_data=TestimonialData(name=feedback_user_name,email=feedback_user_email,feedback=feedback)
        feedback_data.save()

    return render(request,'testimonial.html',)


