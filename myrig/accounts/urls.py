from django.conf.urls import patterns, include, url

urlpatterns = patterns('myrig.accounts.views',
    
    # Login and logout views
    url(r'^login/$',  'login',  name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    
    # URLs for OpenID authentication
    url('', include('social.apps.django_app.urls', namespace='social')),
    
    # User profile page and tools
    url(r'^profile/$',                     'profile', name='profile'),
    url(r'^profile/change-display-name/$', 'change_display_name'),
)
