from talks.models import Proposal
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.module_loading import import_string
from django.utils.translation import ugettext as _

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from markitup.widgets import MarkItUpWidget


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ('title', 'talk_type', 'abstract', 'experience_level')
        widgets = {
            'abstract': MarkItUpWidget(),
          }

    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.add_input(Submit('send', 'Submit'))
        self.helper.form_class = 'form-horizontal'

