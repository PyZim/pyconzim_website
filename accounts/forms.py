from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class RegistrationForm(UserCreationForm):
    
    email = forms.CharField(max_length=75, required=True)

    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout('first_name',
                                    'last_name',
                                    'email',
                                    'username',
                                    'password1',
                                    'password2',
                                    )
        self.helper.add_input(Submit('signup', 'Sign up'))


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            'username',
            'password',
        )
        self.helper.add_input(Submit('login', 'Log in'))
