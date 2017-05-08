from talks.models import Proposal
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from markitup.widgets import MarkItUpWidget


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ('title', 'talk_type', 'abstract', 'experience_level', 'notes',)

        widgets = {
            'abstract': MarkItUpWidget(),
          }

    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'
