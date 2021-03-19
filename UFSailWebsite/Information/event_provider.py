from .models import Event
from datetime import datetime, timedelta

class TestEventProvider:
    def get_events(self, day, month, year):
        if day == 19 and month == 3 and year == 2021:
            return [Event(title='test',
                            description='test event',
                            start=datetime.now(),
                            end=datetime.now() + timedelta(hours=1) )]

    def get_repeating_events(self, day, month, year):
        pass

class DatabaseEventProvider:
    def get_events(self, day, month, year):
        events = Event.objects.filter(start__year=year, start__month=month, start__day=day)
        return events.order_by('start__minute')