# In production set the environment variable to :
# DJANGO_SETTINGS_MODULE=indaba.settings.production
from indaba.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Must mention ALLOWED_HOSTS in production!
ALLOWED_HOSTS = ["zw.pycon.org"]
