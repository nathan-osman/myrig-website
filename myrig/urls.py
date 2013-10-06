from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    # Home page
    url(r'^$', 'myrig.views.index', name='home'),
    
    # Administration interface
    url(r'^admin/', include(admin.site.urls)),
)

# When running in DEBUG mode, serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
