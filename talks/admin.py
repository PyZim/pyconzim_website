from django.contrib import admin
from .models import Proposal


class TalkAdmin(admin.ModelAdmin):
    list_display = ("title", "talk_type",)
    list_editable = ('status')

admin.site.register(Proposal)

