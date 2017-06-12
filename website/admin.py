from django.contrib import admin
from .models import Contact, Subscription


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "email", "message", "email_date")
    list_filter = ["name", "company", "email_date"]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscription)
