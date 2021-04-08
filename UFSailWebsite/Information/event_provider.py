from .models import Event
from datetime import datetime, timedelta

class DatabaseEventProvider:
    def get_events(self, day, month, year):
        events = Event.objects.filter(date__year=year, date__month=month, date__day=day)
        return events.order_by('starttime__hour', 'starttime__minute')

# class TestEventProvider:
#     def get_events(self, day, month, year):
#         if day == 19 and month == 3 and year == 2021:
#             return [Event(title='test',
#                             description='test event',
#                             start=datetime.now(),
#                             end=datetime.now() + timedelta(hours=1))]