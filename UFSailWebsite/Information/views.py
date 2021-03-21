from django.shortcuts import render
from .models import Officer, Event
from .custom_calendar import Calendar
from .event_provider import TestEventProvider, DatabaseEventProvider
from django.utils.safestring import mark_safe
from datetime import date

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
    # get month offset as query param, default to 0
    try:
        offset = int(request.GET.get('month_offset', 0))
    except ValueError:
        offset = 0

    today = date.today() # TODO: localize?

    # This looks gross, but mainly because python stores months 1-12 rather than 0-11
    # Works because python handles modulo and integer division on negative numbers 
    # in a convenient (complementary) manner
    year = today.year + (today.month - 1 + offset)//12 
    month = 1 + (today.month - 1 + offset) % 12

    cal = Calendar(DatabaseEventProvider())
    html_cal = cal.formatmonth(year, month)

    events = Event.objects.all()[:3]

    context = {
        'current_item' : 'events',
        'calendar' : mark_safe(html_cal),
        'prev' : offset - 1,
        'next' : offset + 1,
        'upcoming_events' : events
    }

    return render(request, 'Information/events.html', context)

def forms(request):
    if request.method == 'POST':
        print(request)
    context = {
        'current_item' : 'forms'
    }
    return render(request, 'Information/forms.html', context)