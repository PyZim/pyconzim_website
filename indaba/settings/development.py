# from indaba.settings.base import *
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
INSTALLED_APPS += (
    'slack_invitation',
)

DJANGO_SLACK_INVITATION_TEAM = 'pyconzim2017'
DJANGO_SLACK_INVITATION_TOKEN = 'your-slack-token'
