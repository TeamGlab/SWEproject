from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
import pytz

class Officer(models.Model):
    firstname = models.CharField('first name', max_length=50)
    lastname = models.CharField('last name', max_length=50)
    role = models.CharField('role', max_length=50)
    email = models.CharField('email', max_length=50)
    bio = models.TextField('bio')
    image = models.ImageField(upload_to='officer_profiles/') 

    # Get a human-readable representation of the object
    def __str__(self):
        return f"{self.firstname} {self.lastname}: {self.role}"

    def fullname(self):
    	return f"{self.firstname} {self.lastname}"


class Event(models.Model):
    title = models.CharField('event title', max_length=200)
    description = models.TextField('event description', blank=True, default='')
    location = models.CharField('location', max_length=100, blank=True, default='')
    date = models.DateField('date')
    starttime = models.TimeField('start time')
    endtime = models.TimeField('end time')
    link = models.URLField('link (optional)', max_length=200, blank=True, default='')

    # Get a human-readable representation of the object
    def __str__(self):
        return f"{self.title}: {self.description}"

    def has_passed(self):
        end = datetime.datetime.combine(self.date, self.endtime)
        return end <= timezone.now()

    def get_day(self):
        start = datetime.datetime.combine(self.date, self.starttime)
        return f"{start.day:02d}"

    def get_month_abbr(self):
        start = datetime.datetime.combine(self.date, self.starttime)
        return start.strftime('%b')

    def get_time_string(self):
        timezone.activate(pytz.timezone("US/Eastern"))
        start = timezone.make_aware(datetime.datetime.combine(self.date, self.starttime))
        end = timezone.make_aware(datetime.datetime.combine(self.date, self.endtime))
        s = f"{to_standard(start.hour)}:{start.strftime('%M %p')}"
        e = f"{to_standard(end.hour)}:{end.strftime('%M %p')}"
        return f'{s} to {e}'

    def calendar_display_time(self):
        timezone.activate(pytz.timezone("US/Eastern"))
        start = timezone.make_aware(datetime.datetime.combine(self.date, self.starttime))
        return f"{to_standard(start.hour)}:{start.strftime('%M%p')}"

    # Used for validation in admin forms
    def clean(self):
        if self.endtime <= self.starttime:
            raise ValidationError("Event end time must be after the start time.")


def to_standard(hour):
    mod = hour % 12
    return 12 if mod == 0 else mod

class EmailMember(models.Model):
    email = models.EmailField()


