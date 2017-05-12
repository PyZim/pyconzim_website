from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from rest_framework import routers

from talks import views
from talks.views import TalkViewsSets

app_name = 'talks'
router = routers.DefaultRouter()
router.register(r'talks', TalkViewsSets)

urlpatterns = [
    url(r'^submit_talk', login_required(views.submit_talk), name='submit_talk'),
    url(r'^talk_list', login_required(views.TalkList.as_view()), name='talk_list'),
    url(r'^edit_talk/(?P<pk>\d+)/$', login_required(views.TalkView.as_view()), name='edit_talk'),
    url(r'^submitted', login_required(views.SuccessView.as_view()), name='submitted'),
    ]

urlpatterns += router.urls
