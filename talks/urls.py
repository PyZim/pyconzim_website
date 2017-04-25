from django.conf.urls import url
from talks.views import CreateTalk, TalkView, TalkList, SuccessView


app_name = 'talks'

urlpatterns = [
    url(r'^submit_talk', CreateTalk.as_view(), name='submit_talk'),
    url(r'^talk_list', TalkList.as_view(), name='talk_list'),
    url(r'^talk/(?P<pk>\d+)/$', TalkView.as_view(), name='view_talk'),
    url(r'^submitted', SuccessView.as_view(), name='submitted'),
    ]

