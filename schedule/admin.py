from django.contrib import admin

from .models import TalkSchedule, Event, Day

admin.site.register(TalkSchedule)
admin.site.register(Event)
admin.site.register(Day)
