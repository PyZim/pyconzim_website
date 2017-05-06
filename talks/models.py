from django.db import models
from markitup.fields import MarkupField
from django.core.urlresolvers import reverse
from django.conf import settings


class Proposal(models.Model):
    TALK_TYPES = (
        ('K', "Keynote Talk - 45 mins"),
        ('S', "Short Talk - 30 mins"),
        ('L', "Long Talk - 1 hour"),
        ('T', "Tutorial - 2 hours or more"),
    )

    STATUS = (('S', 'Submitted'),
              ('A', 'Accepted'),
              ('W', 'Waiting List'),
              ('R', 'Rejected'),)

    EXPERIENCE_LEVEL = (('B', 'Beginner, no prior knowledge of Python required'),
                        ('A', 'Average, some prior knowledge of Python required '),
                        ('G', 'Good Python programmers level'),
                        ('E', 'Experienced Python programmers level'))


    # proposal = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=1024)
    abstract = MarkupField(help_text="Describe what your talk is about")
    notes = models.TextField(
        default='',
        help_text="Anything else you would want the organizers to know."
        "Wi-fi requirments, if tutorial, number of people you can manage e.t.c"
        "This will note be published on website"
    )
    talk_type = models.CharField(choices=TALK_TYPES, max_length=1)
    proposal_id = models.AutoField(primary_key=True, default=None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="proposals", default='')
    status = models.CharField(choices=STATUS, max_length=1, default='')
    experience_level = models.CharField(choices=EXPERIENCE_LEVEL, max_length=1, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
