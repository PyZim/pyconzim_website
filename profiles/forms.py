from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import Profile


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',  'location', 'birth_date', 'contact_number', 'home_page', 'twitter_handle', 'github_username')

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_UpdateForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('update', 'Update Profile'))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_UserForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('update', 'Update Profile'))


class PasswordForm(SetPasswordForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_UserForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.Layout(
            'password1',
            'password2'
        )
        self.helper.add_input(Submit('update', 'Update Profile'))
