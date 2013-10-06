from django.conf.urls import patterns, include, url

urlpatterns = patterns('myrig.accounts.views',
    
    # Login and logout views
    url(r'^login/$',  'login',  name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    
    # URLs for OpenID authentication
    url('', include('social.apps.django_app.urls', namespace='social')),
)
