from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User

from datetime import datetime

from .forms import UpdateForm, UserForm, PasswordForm
from .models import Profile


class ProfileView(TemplateView):
    template_name = "profiles/home.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['title'] = "My Profile"
        context['year'] = datetime.now().year
        context['details'] = User.objects.filter(username=self.request.user)
        try:
            user_profile = Profile.objects.filter(user=self.request.user)
        except Profile.DoesNotExist:
            context['user_profile'] = ''

        else:
            context['user_profile'] = user_profile
        return context


class CreateProfileView(TemplateView):
    template_name = "profiles/create_profile.html"
    # success_url = reverse_lazy('profiles:success')

    def get_context_data(self, **kwargs):
        context = super(CreateProfileView, self).get_context_data(**kwargs)
        context['title'] = 'Create Profile'
        context['form'] = UpdateForm()
        context['year'] = datetime.now().year
        return context

    def post(self, request):
        profile_form = UpdateForm(request.POST)
        if profile_form.is_valid():
            # process the data in request_form.cleaned_data as required
            obj = Profile()  # gets new object
            obj.user = self.request.user
            obj.bio = profile_form.cleaned_data['bio']
            obj.location = profile_form.cleaned_data['location']
            obj.birth_date = profile_form.cleaned_data['birth_date']
            obj.contact_number = profile_form.cleaned_data['contact_number']
            obj.home_page = profile_form.cleaned_data['home_page']
            obj.twitter_handle = profile_form.cleaned_data['twitter_handle']
            obj.github_username = profile_form.cleaned_data['github_username']
            # finally save the object in db
            obj.save()
            return reverse_lazy('profile:success')


class UpdateProfileView(UpdateView):
    form_class = UpdateForm
    model = Profile
    template_name = "profiles/update.html"
    success_url = reverse_lazy('profiles:success')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        try:
            profile = get_object_or_404(User, pk=self.request.user.pk)
        except User.DoesNotExist:
            context['profile'] = ''
            return HttpResponseRedirect('profiles:create_profile')

        else:
            context['profile'] = profile
            context['title'] = 'Update Profile'
        context['year'] = datetime.now().year
        return context


class UpdateLoginView(TemplateView):
    form_class = UserForm
    model = User
    template_name = "profiles/login_details.html"
    success_url = reverse_lazy('profiles:success')

    def get_context_data(self, **kwargs):
        context = super(UpdateLoginView, self).get_context_data(**kwargs)
        try:
            profile = User.objects.get(pk=self.request.user.pk)
        except User.DoesNotExist:
            context['profile'] = ''

        else:
            context['profile'] = profile
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['title'] = 'Update Login Details'
        context['year'] = datetime.now().year
        return context


class PasswordView(TemplateView):
    # form_class = PasswordForm
    model = User
    template_name = "profiles/password.html"
    success_url = reverse_lazy('profiles:success')

    def get_context_data(self, **kwargs):
        context = super(PasswordView, self).get_context_data(**kwargs)
        context['title'] = 'Change Password'
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['form'] = PasswordForm()
        context['year'] = datetime.now().year
        return context


class SuccessView(TemplateView):
    template_name = "profiles/success.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['title'] = 'Profile Update Successful'
        context['categories'] = get_category()
        context['meetups'] = get_meetup()
        context['year'] = datetime.now().year
        return context
