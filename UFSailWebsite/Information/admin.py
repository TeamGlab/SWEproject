from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from .models import Officer, Event, EmailMember
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# For exporting EmailMember data
class EmailMemberResource(resources.ModelResource):
    class Meta:
        model = EmailMember

class EmailMemberAdmin(ImportExportModelAdmin):
    resource_class = EmailMemberResource


# Hide default sections
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)

# Make officer and event details editable by admins
admin.site.register(Officer)
admin.site.register(Event)
admin.site.register(EmailMember, EmailMemberAdmin)

# Customize text above login
admin.site.site_header = 'Officer Administration'
admin.site.index_title = 'Edit or view items below'

