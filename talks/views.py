from django.shortcuts import reverse, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, ListView

from datetime import datetime

# from django.contrib.auth.models import User

from .models import Proposal
from .forms import ProposalForm


class CreateTalk(TemplateView):
    template_name = "talks/talk_form.html"

    def get_context_data(self, **kwargs):
        context = super(CreateTalk, self).get_context_data(**kwargs)
        context['title'] = "Submit Talk"
        context['form'] = ProposalForm()
        context['year'] = datetime.now().year
        return context

    def post(self, request):
        talk_form = ProposalForm(request.POST)
        if talk_form.is_valid():
            # process the data in request_form.cleaned_data as required
            obj = Proposal()  # gets new object
            obj.author = self.request.user
            obj.title = talk_form.cleaned_data['title']
            obj.abstract = talk_form.cleaned_data['abstract']
            obj.talk_type = talk_form.cleaned_data['talk_type']
            obj.experience_level = talk_form.cleaned_data['experience_level']
            # finally save the object in db
            obj.save()
            return reverse_lazy('talks:submitted')


class TalkView(UpdateView):
    template_name = "talks/talk.html"
    form_class = ProposalForm
    model = Proposal
    success_url = reverse_lazy('talks:success')

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
        context['title'] = 'Talk Submission Successful'
        context['year'] = datetime.now().year
        return context
