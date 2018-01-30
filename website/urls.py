from django.conf.urls import url
from website import views


app_name = 'website'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'accommodation', views.accommodation, name='accommodation'),
    url(r'cofc', views.cofc, name='cofc'),
    url(r'manifesto', views.manifesto, name='manifesto'),
    url(r'venue', views.venue, name='venue'),
    url(r'contact', views.contact, name='contact'),
    url(r'subscribe', views.subscribe, name='subscribe'),
    url(r'success', views.success, name='success'),
    url(r'thanks', views.thanks, name='thanks'),
    url(r'registration', views.registration, name='registration'),
    url(r'sprints', views.sprints, name='sprints'),
    url(r'2017', views.pyconzim_2017, name='pyconzim_2017'),
]
