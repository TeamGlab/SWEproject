from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from .models import Event
from .custom_calendar import Calendar

class TestCalendar(TestCase):
	
	def setUp(self):
		pass