from django.conf.urls import url

from schedule import views


app_name = 'schedule'

urlpatterns = [
    url(r'', views.schedule, name='schedule'),

]
