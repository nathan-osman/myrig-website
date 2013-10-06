'''
NOTE: this file contains installation-dependent settings
Do not put global settings in this file
Instead, put them in settings.py
'''

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
SECRET_KEY = '6_*l@$bqnl)36(tci-lo&lwa)))t$b=pi688bl9m3*+xunf(yt'
