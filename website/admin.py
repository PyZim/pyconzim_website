from django.contrib import admin

from .models import Contact, Subscription, Sponsor

admin.site.register(Contact)
admin.site.register(Subscription)
admin.site.register(Sponsor)
