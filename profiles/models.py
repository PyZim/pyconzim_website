from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=16, null=True, blank=True)
    home_page = models.CharField(max_length=255)
    twitter_handle = models.CharField(max_length=15)
    github_username = models.CharField(max_length=32)

    def __str__(self):
        return u'%s' % self.user