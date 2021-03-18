from django.db import models

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
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')

    # Get a human-readable representation of the object
    def __str__(self):
        return f"{self.title}: {self.description}"

    def has_passed(self):
        return self.end <= timezone.now()