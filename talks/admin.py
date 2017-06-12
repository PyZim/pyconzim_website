from django.contrib import admin
from .models import Proposal


class TalkAdmin(admin.ModelAdmin):
    list_display = ("title", "talk_type", "experience_level", "status")
    list_editable = ["status"]
    list_filter = ("talk_type", "status")

admin.site.register(Proposal, TalkAdmin)

