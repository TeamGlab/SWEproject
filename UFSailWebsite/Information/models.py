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
