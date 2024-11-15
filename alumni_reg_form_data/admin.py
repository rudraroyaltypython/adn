from django.contrib import admin
from django.http import HttpResponse
from alumni_reg_form_data.models import AlumniRegFormData
import csv


def export_alumni_to_csv(modeladmin, request, queryset):
    # Create the HttpResponse object with CSV headers.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="alumni_data.csv"'

    # Initialize the CSV writer
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(['First Name','Father/Husband Name','Last Name','Address','Taluka','District','State','Country','Mobile No (Whatsapp No)','Email','Passed Out from the class','Year of Passing Out','Present Qualification','Present Designation'])

    # Write data rows
    for alumni in queryset:
        writer.writerow([alumni.first_name,alumni.father_or_husband_name,alumni.surname,alumni.address,alumni.taluka,alumni.district,alumni.state,alumni.country,alumni.mobile_no,alumni.email_id,alumni.passed_out_from_class,alumni.year_of_passing_out,alumni.present_qualification,alumni.present_designation])

    return response

export_alumni_to_csv.short_description = "Export selected alumni to CSV"




class AlumniRegFormDataAdmin(admin.ModelAdmin):
    list_display=['first_name','father_or_husband_name','surname','address','taluka','district','state','country','mobile_no','email_id','passed_out_from_class','year_of_passing_out','present_qualification','present_designation']
    actions = [export_alumni_to_csv]
# Register your models here.

admin.site.register(AlumniRegFormData,AlumniRegFormDataAdmin)



