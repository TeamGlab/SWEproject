from django.contrib import admin
from .models import Officer, Event, EmailMember

# Make officer and event details editable by admins
admin.site.register(Officer)
admin.site.register(Event)
admin.site.register(EmailMember)

