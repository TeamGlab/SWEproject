from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('contact/', contact, name = 'contact'),
    path('events/', events, name = 'events'),
    path('forms/', forms, name = 'forms')
]