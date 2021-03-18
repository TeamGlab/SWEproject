from django.shortcuts import render
from .models import Officer, Event
from .custom_calendar import Calendar
import calendar
from django.utils.safestring import mark_safe

def home(request):
    context = {
        'current_item' : 'home'
    }
    return render(request, 'Information/home.html', context)

def contact(request):
    officers = Officer.objects.all()
    # TODO: order officers properly
    context = {
        'current_item' : 'contact',
        'officers' : officers
    }
    return render(request, 'Information/contact.html', context)

def events(request):
    cal = Calendar(calendar.SUNDAY)
    html_cal = cal.formatmonth(2020, 3)

    events = Event.objects.all()
    context = {
        'current_item' : 'events',
        'calendar' : mark_safe(html_cal),
        'upcoming_events' : events
    }
    return render(request, 'Information/events.html', context)

def forms(request):
    context = {
        'current_item' : 'forms'
    }
    return render(request, 'Information/forms.html', context)