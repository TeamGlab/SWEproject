from django.db import models
from django.utils import timezone
import pytz


# Create your models here.
# TODO: add model for officer, use to store officer bios, img, etc?
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
    description = models.TextField('event description')
    location = models.CharField('location', max_length=100, blank=True, default='')
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')
    link = models.URLField('optional link', max_length=200, blank=True, default='')

    # Get a human-readable representation of the object
    def __str__(self):
        return f"{self.title}: {self.description}"

    def has_passed(self):
        return self.end <= timezone.now()

    def get_day(self):
        return self.start.day

    def get_month_abbr(self):
        return self.start.strftime('%b')

    def get_time_string(self):
        timezone.activate(pytz.timezone("US/Eastern")) # TODO: localize?
        start = timezone.localtime(self.start)
        end = timezone.localtime(self.end)
        s = f"{start.hour%12}:{start.strftime('%M %p')}"
        e = f"{end.hour%12}:{end.strftime('%M %p')}"
        return f'{s} to {e}'

    def calendar_display_text(self):
        timezone.activate(pytz.timezone("US/Eastern")) # TODO: localize?
        start = timezone.localtime(self.start)
        return f"{start.hour%12}:{start.strftime('%M%p')} {self.title}"

