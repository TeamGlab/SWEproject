from django.shortcuts import render
from .models import Officer, Event, EmailMember
from .custom_calendar import Calendar
from .event_provider import TestEventProvider, DatabaseEventProvider
from .forms import EmailForm
from django.http import HttpResponseRedirect, HttpResponse
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
    cal = Calendar(DatabaseEventProvider())
    html_cal = cal.formatmonth(2021, 3)

    events = Event.objects.all()
    context = {
        'current_item' : 'events',
        'calendar' : mark_safe(html_cal),
        'upcoming_events' : events
    }
    return render(request, 'Information/events.html', context)

def forms(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            p = EmailMember(email=email)
            p.save()
            return HttpResponseRedirect('/forms/')
    else:
        form = EmailForm()
    context = {
        'current_item' : 'forms',
    }
    return render(request, 'Information/forms.html', {'form' : form})
