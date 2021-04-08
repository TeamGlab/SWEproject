from django.contrib import admin
from .models import Officer, Event, EmailMember
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# For exporting EmailMember data
class EmailMemberResource(resources.ModelResource):
    class Meta:
        model = EmailMember

class EmailMemberAdmin(ImportExportModelAdmin):
    resource_class = EmailMemberResource


# Make officer and event details editable by admins
admin.site.register(Officer)
admin.site.register(Event)
admin.site.register(EmailMember, EmailMemberAdmin)

