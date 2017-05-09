from django.db import models
from django.contrib.auth.models import User

from libgravatar import Gravatar


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, help_text="Tell us a bit about yourself and your work with Python", blank=True)
    location = models.CharField(max_length=30, help_text="City, Country", blank=True)
    birth_date = models.DateField(null=True, help_text="Please enter your date of birth in the format YYYY-MM-DD", blank=True)
    contact_number = models.CharField(max_length=16, help_text="Please include your country code.", null=True, blank=True)
    home_page = models.CharField(max_length=255, help_text="Your website/blog URL.")
    twitter_handle = models.CharField(max_length=15)
    github_username = models.CharField(max_length=32)

    def get_avatar_url(self, email):
        # email = self.user.email
         g = Gravatar(email)
         return g.get_image()

    def __str__(self):
        return u'%s' % self.user

