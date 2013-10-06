'''
NOTE: this file contains installation-dependent settings
Do not put global settings in this file
Instead, put them in settings.py
'''

# Uncomment the next two lines when developing locally
#DEBUG          = True
#TEMPLATE_DEBUG = True

# Database storage engine(s) for the project
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.',
        'NAME':     '',
        'USER':     '',
        'PASSWORD': '',
        'HOST':     '',
        'PORT':     '',
    },
}

# Absolute filesystem path where media (uploaded) and static files will be stored
MEDIA_ROOT  = ''
STATIC_ROOT = ''

# URL for media and static files
MEDIA_URL  = '/media/'
STATIC_URL = '/static/'

# This needs to be a unique string
SECRET_KEY = ''
