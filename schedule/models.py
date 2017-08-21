from django.db import models
from django.utils import timezone

from talks.models import Proposal


DAY_SESSIONS = (
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening'),
)
ROOMS = (('Room 1', 'Room 1'),
         ('Room 2', 'Room 2'))


class Day(models.Model):
    conference_day = models.CharField(max_length=30)

    class Meta:
        managed = True

    def __str__(self):
        return self.conference_day


class TalkSchedule(models.Model):
    conference_day = models.ForeignKey(Day)
    talk = models.ForeignKey(Proposal)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    day_session = models.CharField(max_length=10, choices=DAY_SESSIONS, default='')
    room = models.CharField(max_length=10, choices=ROOMS, default='')

    class Meta:
        managed = True
        verbose_name_plural = "talk Schedule"

    def __str__(self):
        return self.room


class Event(models.Model):
    name = models.CharField(max_length=50)
    conference_day = models.ForeignKey(Day)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    day_session = models.CharField(max_length=10, choices=DAY_SESSIONS, default='')
    room = models.CharField(max_length=10, choices=ROOMS, default='')

    class Meta:
        managed = True

    def __str__(self):
        return self.name