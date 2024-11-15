from django.contrib import admin
from django.http import HttpResponse
import csv
from newsletter.models import SubscribeNewsletter

def export_subscribe_newsletter_to_csv(modeladmin, request, queryset):
    # Create the HttpResponse object with CSV headers.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="subscribe_newsletter_data.csv"'

    # Initialize the CSV writer
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(['Email'])

    # Write data rows
    for contact in queryset:
        writer.writerow([contact.mail])

    return response

export_subscribe_newsletter_to_csv.short_description = "Export selected subscribe_newsletter_data to CSV"


class SubscribeNewsletterAdmin(admin.ModelAdmin):
    list_display=['mail']
    actions = [export_subscribe_newsletter_to_csv]


# Register your models here.

admin.site.register(SubscribeNewsletter,SubscribeNewsletterAdmin)