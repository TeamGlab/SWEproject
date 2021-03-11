from django.contrib import admin
from .models import Officer

# Make officer details editable by admins
admin.site.register(Officer)
