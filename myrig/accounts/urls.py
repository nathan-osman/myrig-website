from django.conf.urls import patterns, include, url

urlpatterns = patterns('myrig.accounts.views',
    
    # Login form
    url(r'^login/$', 'login', name='login'),
    
    # URLs for OpenID authentication
    url('', include('social.apps.django_app.urls', namespace='social')),
)
