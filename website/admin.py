from django.contrib import admin
from .models import Contact, Subscription, Sponsor


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "email", "message", "email_date")
    list_filter = ["name", "company", "email_date"]


class SponsorAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "type")
    list_filter = ["category", "type"]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscription)
admin.site.register(Sponsor, SponsorAdmin)
