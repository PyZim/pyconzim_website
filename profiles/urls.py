from django.conf.urls import url

from .views import UpdateProfileView, ProfileView, UpdateLoginView, CreateProfileView, PasswordView


app_name = 'profiles'

urlpatterns = [
    url(r'create_profile/$', CreateProfileView.as_view(), name='create_profile'),
    url(r'update/(?P<pk>\d+)/$', UpdateProfileView.as_view(), name='update'),
    url(r'home/$', ProfileView.as_view(), name='profile_home'),
    url(r'login_details/password/$', PasswordView.as_view(), name='password'),
    url(r'login_details/(?P<pk>\d+)/$', UpdateLoginView.as_view(), name='login_details'),
]
