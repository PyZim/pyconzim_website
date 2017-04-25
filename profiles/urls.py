from django.conf.urls import url

from .views import UpdateProfileView, ProfileView, UpdateLoginView, CreateProfileView, PasswordView, SuccessView


app_name = 'profiles'

urlpatterns = [
    url(r'create_profile/$', CreateProfileView.as_view(), name='create_profile'),
    url(r'update/(?P<pk>\d+)/$', UpdateProfileView.as_view(), name='update'),
    url(r'home/$', ProfileView.as_view(), name='profile_home'),
    url(r'password_change/(?P<pk>\d+)/$', PasswordView.as_view(), name='password_change'),
    url(r'login_details/(?P<pk>\d+)/$', UpdateLoginView.as_view(), name='login_details'),
    url(r'profile_update/$', SuccessView.as_view(), name='profile_update'),
]
