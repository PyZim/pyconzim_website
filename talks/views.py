from django.shortcuts import reverse, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    TemplateView,
    UpdateView,
    ListView,
)

from datetime import datetime

from django.contrib.auth.models import User

from .models import Proposal
from .forms import ProposalForm


class CreateTalk(LoginRequiredMixin, CreateView):
    model = Proposal
    form_class = ProposalForm
    template_name = "talks/talk_form.html"
    permission_denied_message = 'Please login or register to submit a talk'

    def get_permission_denied_message(self):
        return self.permission_denied_message
    
    def get_form_kwargs(self):
        kwargs = super(CreateTalk, self).get_form_kwargs()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreateTalk, self).get_context_data(**kwargs)
        context['title'] = "Submit Talk"
        context['year'] = datetime.now().year
        return context
    
    def get_form_valid_message(self):
        msg = ugettext('Talk proposal <strong>{title}</strong> created.')
        return format_html(msg, title=self.object.title)
    

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        
        # Save the author information as well (many-to-many fun)
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())


class TalkView(UpdateView):
    template_name = "talks/talk.html"
    form_class = ProposalForm
    model = Proposal
    success_url = reverse_lazy('talks:success')

    def get_object(self,*args, **kwargs):
        object = super(TalkView, self).get_object(*args, **kwargs)
        return object

    def get_context_data(self, **kwargs):
        context = super(TalkView, self).get_context_data(**kwargs)
        context['title'] = "Talk Details"
        context['year'] = datetime.now().year
        context['submitted_talks'] = get_object_or_404(Proposal, pk=Proposal.pk)
        return context


class TalkList(ListView):
    template_name = "talks/talk_list.html"

    def get_context_data(self, **kwargs):
        context = super(TalkList, self).get_context_data(**kwargs)
        context['title'] = "Submitted Talks"
        context['year'] = datetime.now().year
        context['submitted_talks'] = get_object_or_404(Proposal, author=self.request.user)
        return context


class SuccessView(TemplateView):
    template_name = "talks/success.html"

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['title'] = 'Talk Update Successful'
        context['year'] = datetime.now().year
        return context
