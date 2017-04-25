from django.conf.urls import url

from .views import SignUpView, LoginView, LogOutView, SuccessView


app_name = 'accounts'

urlpatterns = [
    url(r'register/$', SignUpView.as_view(), name='signup'),
    url(r'accounts/login/$', LoginView.as_view(), name='login'),
    url(r'accounts/logout/$', LogOutView.as_view(), name='logout'),
    url(r'success/$', SuccessView.as_view(), name='success'),
]
