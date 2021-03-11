from django.shortcuts import render
from .models import Officer


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
    context = {
        'current_item' : 'events'
    }
    return render(request, 'Information/events.html', context)