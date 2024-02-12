from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')  # Modify according to your actual model fields
    # list_filter = ('subject',)  # Add a filter for the 'subject' field
    search_fields = ('name', 'email', 'subject', 'message')  # Add search functionality
    actions = ['export_csv']

    def export_csv(self, request, queryset):
        # Create a response object with CSV content type
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="contacts.csv"'

        # Create a CSV writer using the response object
        writer = csv.writer(response)

        # Write the header row
        writer.writerow(['Name', 'Email', 'Subject', 'Message'])

        # Write the data rows
        for contact in queryset:
            writer.writerow([contact.name, contact.email, contact.message])

        return response

    export_csv.short_description = "Export selected contacts to CSV"

# Register the Contact model with the modified ContactAdmin
admin.site.register(Contact, ContactAdmin)
