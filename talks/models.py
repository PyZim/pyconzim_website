from django.db import models
from markitup.fields import MarkupField
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Proposal(models.Model):
    TALK_TYPES = (
        ('Keynote', "Keynote Talk - 45 mins"),
        ('Short Talk', "Short Talk - 30 mins"),
        ('Long Talk', "Long Talk - 1 hour"),
        ('Tutorial', "Tutorial - 2 hours or more"),
    )

    STATUS = (('S', 'Submitted'),
              ('A', 'Accepted'),
              ('W', 'Waiting List'),
              ('R', 'Rejected'),)

    EXPERIENCE_LEVEL = (('Beginners', 'Beginners, no prior knowledge of Python required'),
                        ('Mid-level Programmers', 'Average, some prior knowledge of Python required'),
                        ('Senior Programmers', 'Good Python programmers level'),
                        ('Expert Programmers', 'Experienced Python programmers level'))

    # proposal = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=1024)
    abstract = MarkupField(help_text="Describe what your talk is about")
    talk_type = models.CharField(choices=TALK_TYPES, max_length=20)
    proposal_id = models.AutoField(primary_key=True, default=None)
    notes = models.TextField(default='', help_text = "Anything else you would want the organizers to know." 
                             "Wi-fi requirments, if tutorial, number of people you can manage e.t.c."
                             "This will not be published on website.", blank=True, null=True
                             )
    user = models.ForeignKey(User, related_name="proposals", default='')
    status = models.CharField(choices=STATUS, max_length=1, default='')
    experience_level = models.CharField(choices=EXPERIENCE_LEVEL, max_length=30, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
