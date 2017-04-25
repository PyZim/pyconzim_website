from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect


from datetime import datetime


def schedule(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'schedule/schedule.html',
        {
            'title': 'Schedule',
            'message': 'Schedule',
            'year': datetime.now().year,
        }
    )