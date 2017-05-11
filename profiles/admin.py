from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "email_address", "contact_number", "location")
    list_filter = ["location"]


admin.site.register(Profile, ProfileAdmin)
