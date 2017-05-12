# In production set the environment variable to :
# DJANGO_SETTINGS_MODULE=indaba.settings.production
from indaba.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Must mention ALLOWED_HOSTS in production!
ALLOWED_HOSTS = ["zw.pycon.org"]

# app secret has been cchanged for production
SECRET_KEY = '1nknhf9s0e@q87^*!4nc9$8c@797+$=c09bfnm#5&p=w56#n5&)zydl%vx7b*u9d2j3p-2p!*o2%eog'

# Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'zim.pycon@gmail.com'
EMAIL_HOST_PASSWORD = 'amrtivdcddenkulw'

# captcha settings for production
RECAPTCHA_PUBLIC_KEY = '6LexKiEUAAAAAGlxwMYHWlwqf3yHwdbwPaLT8omK'
RECAPTCHA_PRIVATE_KEY = '6LexKiEUAAAAABLwx8uU4xyLwZYefOASqDSxDSEZ'
