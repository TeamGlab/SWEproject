from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from .models import Officer, Event, to_standard
from .custom_calendar import Calendar
from datetime import datetime, timedelta, time
from .event_provider import DatabaseEventProvider

class TestOfficer(TestCase):
	def setUp(self):
		self.testOfficer = Officer(firstname='First', lastname='Last', 
								role='President', email='test@email.com', 
								bio='Bio')
		self.testOfficer.save()

	def test__str__(self):
		assert(str(self.testOfficer) == "First Last: President")

	def testFullName(self):
		assert(self.testOfficer.fullname() == "First Last")


class TestCalendar(TestCase):
	
	def setUp(self):
		self.pastEvent = Event(title='past', description='test', location='nowhere', 
								date=datetime.today() - timedelta(days=1), 
								starttime=time(2, 30), 
								endtime=time(3, 30))
		self.pastEvent.save()
		self.futureEvent = Event(title='future', description='test', location='nowhere', 
								date=datetime.today() + timedelta(days=1), 
								starttime=time(2, 30), 
								endtime=time(3, 30))
		self.futureEvent.save()
		self.testEvent = Event(title='test', description='test', location='nowhere', 
								date=datetime(2021, 5, 2), 
								starttime=time(2, 30), 
								endtime=time(3, 30))
		self.testEvent.save()
		for i in range(1,6):
			event = Event(title=f'test{i}', description='test', location='nowhere', 
								date=datetime(2021, 5, 4), 
								starttime=time(i, 30), 
								endtime=time(i+1, 30))
			event.save()


	def testEventProvider(self):
		provider = DatabaseEventProvider()
		assert(len(provider.get_events(2, 5, 2021)) == 1)
		assert(len(provider.get_events(2, 3, 2021)) == 0)
		assert(len(provider.get_events(4, 5, 2021)) == 5)

	def testEventMethods(self):
		assert(self.pastEvent.has_passed())
		assert(not self.futureEvent.has_passed())
		e = self.testEvent
		assert(e.get_day() == "02")
		assert(e.get_month_abbr() == "May")
		assert(e.get_time_string() == "2:30 AM to 3:30 AM")
		assert(e.calendar_display_time() == "2:30AM")

class SimpleTests(SimpleTestCase):
	def testTo_Standard(self):
		hour1 = 24
		hour2 = 12
		hour3 = 3
		hour4 = 18
		assert(to_standard(hour1) == 12)
		assert(to_standard(hour2) == 12)
		assert(to_standard(hour3) == 3)
		assert(to_standard(hour4) == 6)
