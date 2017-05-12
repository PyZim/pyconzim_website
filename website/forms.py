from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from captcha.fields import ReCaptchaField


from .models import Contact, Subscription


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ('name', 'company', 'email', 'message',)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_ContactForm'
        self.helper.form_class = 'form-horizontal'
        # Moving field labels into placeholders
        layout = self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('send', 'Send Message'))

class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_SubscribeForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('send', 'Notify me'))
        # Moving field labels into placeholders
        layout = self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        self.helper.form_show_labels = False
