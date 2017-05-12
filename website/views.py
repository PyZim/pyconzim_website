from __future__ import absolute_import
from django.shortcuts import render, reverse
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages


from datetime import datetime


from .forms import ContactForm, SubscribeForm
from .models import Contact, Subscription, Sponsor


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    contact_form = ContactForm()
    subscribe_form = SubscribeForm()

    corporates = Sponsor.objects.filter(type="C")
    individuals = Sponsor.objects.filter(type="I")

    return render(
        request,
        'website/index.html',
        {
            'title': 'Home',
            'message': 'Home Page',
            'year': datetime.now().year,
            'contact_form': contact_form,
            'subscribe_form': subscribe_form,
            'corporates': corporates,
            'individuals': individuals,
        }
    )


def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            # process the data in contact_form.cleaned_data as required
            obj = Contact()  # gets new object
            obj.name = contact_form.cleaned_data['name']
            obj.company = contact_form.cleaned_data['company']
            obj.email = contact_form.cleaned_data['email']
            obj.message = contact_form.cleaned_data['message']
            # finally save the object in db
            obj.save()

            # send email to pycon_zim@gmail.com
            subject = "Message on Contact Form "
            message = 'A message was submitted on the website\n\n'
            message += 'Name: ' + contact_form.cleaned_data['name'] + '\n'
            message += 'Email: ' + contact_form.cleaned_data['email'] + '\n'
            message += 'Company: ' + contact_form.cleaned_data['company'] + '\n'
            message += 'Message:\n ' + contact_form.cleaned_data['message'] + '\n'

            sender = 'zim.pycon@gmail.com'

            recipient_list = ['zim.pycon@gmail.com']
            send_mail(subject, message, sender, recipient_list)

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('website:thanks'))

    else:
        # if a GET (or any other method) we'll create a blank form
        contact_form = ContactForm()

        return HttpResponseRedirect(reverse('website:home'))


def subscribe(request):
    if request.method == "POST":
        subscribe_form = SubscribeForm(request.POST)

        if subscribe_form.is_valid():
            # process the data in subscribe_form.cleaned_data as required
            obj = Subscription()  # gets new object
            obj.email = subscribe_form.cleaned_data['email']
            # finally save the object in db
            obj.save()

            return HttpResponseRedirect(reverse('website:success'))


"""Renders the success page"""
def success(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'website/success.html',
        {
            'title': 'Success ',
            'message': 'Success',
            'year': datetime.now().year,
        }
    )


"""Renders the thanks page"""
def thanks(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'website/thanks.html',
        {
            'title': 'Message Sent ',
            'message': 'Message sent ',
            'year': datetime.now().year,
        }
    )


def cofc(request):
    """Renders the cofc page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'website/cofc.html',
        {
            'title': 'Code of Conduct',
            'message': 'Code of Conduct',
            'year': datetime.now().year,
        }
    )


def manifesto(request):
    """Renders the manifesto page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'website/manifesto.html',
        {
            'title': 'Manifesto',
            'message': 'Our Manifesto',
            'year': datetime.now().year,
        }
    )


def venue(request):
    """Renders the venue page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'website/venue.html',
        {
            'title': 'Location',
            'message': 'Location',
            'year': datetime.now().year,
        }
    )


def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'website/registration.html',
        {
            'title': 'Registration',
            'message': 'Registration for PyConZim',
            'year': datetime.now().year,
        }
    )


def sprints(request):
    """Renders the sprints venue page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'website/sprints.html',
        {
            'title': 'Sprints Venue',
            'message': 'Sprints Venue',
            'year': datetime.now().year,
        }
    )


def accommodation(request):
    """Renders the accommodation page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'website/accommodation.html',
        {
            'title': 'Location',
            'message': 'Location',
            'year': datetime.now().year,
        }
    )
