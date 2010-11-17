from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.views.generic.simple import direct_to_template
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^mapeo/', include('maonic.mapeo.urls')),

    (r'^$', 'maonic.views.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^files/(.*)$', 'django.views.static.serve',
                            {'document_root': settings.PROJECT_ROOT + '/media'}),
                            )
