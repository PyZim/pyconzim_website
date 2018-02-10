from rest_framework import routers

from talks.views import TalkViewsSets
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from talks import views


app_name = 'talks'
router = routers.DefaultRouter()
router.register(r'talks', TalkViewsSets)


urlpatterns = [
    url(r'^submit_talk', login_required(views.submit_talk), name='submit_talk'),
    # url(r'^talk_list', login_required(views.TalkList.as_view()), name='talk_list'),
    url(r'^edit_talk/(?P<pk>\d+)/$', login_required(views.TalkView.as_view()), name='edit_talk'),
    url(r'^submitted', login_required(views.SuccessView.as_view()), name='submitted'),
    url(r'^accepted_talks', views.AcceptedTalksView.as_view(), name='accepted_talks'),
    # url(r'^talk_details/(?P<pk>\d+)/$', views.TalkDetailView.as_view(), name='talk_details'),
    ]

urlpatterns += router.urls
