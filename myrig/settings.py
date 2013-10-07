# NOTE: this file contains global settings
# Do not put installation-dependent settings in this file
# Instead, put them in local_settings.py

import os.path

# Only requests for myrig.quickmediasolutions.com will be processed
ALLOWED_HOSTS = ['myrig.quickmediasolutions.com',]

SITE_ID = 1

# Enable timezone-aware datetimes
USE_TZ    = True
TIME_ZONE = 'America/Vancouver'

# Determine the directory this file resides in so that an absolute
# path can be specified for the static files and templates
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)
TEMPLATE_DIRS    = (os.path.join(PROJECT_ROOT, 'templates'),)

ROOT_URLCONF     = 'myrig.urls'
WSGI_APPLICATION = 'myrig.wsgi.application'

INSTALLED_APPS = (
    # Core Django applications
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Django helper applications
    'south',
    'widget_tweaks',
    'social.apps.django_app.default',
    # MyRig applications
    'myrig.accounts',
    'myrig.computer',
)

# Authentication backends
AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'django.contrib.auth.backends.ModelBackend',
)

# Import local settings, which may add to or override the above settings
try:
    from local_settings import *
except ImportError:
    pass
