from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView, TemplateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User

from datetime import datetime


class SignUpView(CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:success')

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['title'] = 'Sign up'
        context['year'] = datetime.now().year
        return context


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('website:home')

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'Log in'
        context['year'] = datetime.now().year
        return context

    def form_valid(self,form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

        
class LogOutView(RedirectView):
    url = reverse_lazy('website:home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)


class SuccessView(TemplateView):
    template_name = "accounts/success.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['title'] = 'Registration Successful'
        context['year'] = datetime.now().year
        return context







