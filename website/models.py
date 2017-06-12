from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField("full name", max_length=120)
    company = models.CharField("company name", max_length=120)
    email = models.EmailField("email address", max_length=120)
    message = models.TextField()
    email_date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


class Subscription(models.Model):
   email = models.EmailField("email address", max_length=120)
   date_sub = models.DateTimeField("date subscribed", default=timezone.now)
   is_active = models.BooleanField(default=True)

   class Meta:
       managed = True

   def __str__(self):
       return self.email
