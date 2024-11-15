from django.contrib import admin
from django.contrib import admin
from django.http import HttpResponse
import csv
from contact_us_data.models import ContactUS

def export_contact_us_to_csv(modeladmin, request, queryset):
    # Create the HttpResponse object with CSV headers.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contact_us_data.csv"'

    # Initialize the CSV writer
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(['Name','Father/Husband Name','Email','Subject','Message'])

    # Write data rows
    for contact in queryset:
        writer.writerow([contact.name,contact.mail,contact.subject,contact.message])

    return response

export_contact_us_to_csv.short_description = "Export selected contact_us_data to CSV"



class ContactUSAdmin(admin.ModelAdmin):
    list_display=['name','mail','subject','message']
    actions = [export_contact_us_to_csv]


# Register your models here.

admin.site.register(ContactUS,ContactUSAdmin)

