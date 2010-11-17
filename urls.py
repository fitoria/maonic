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

    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^mapeo/$', direct_to_template, {'template': 'mapeo/index.html'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^files/(.*)$', 'django.views.static.serve',
                            {'document_root': settings.PROJECT_ROOT + '/media'}),
                            )

#urlpatterns += patterns('',
#  (r'^accounts/profile/$', direct_to_template, {'template': 'registration/profile.html'}),
#  (r'^accounts/password_reset/$', password_reset, {'template_name': 'registration/password_reset.html'}),
#  (r'^accounts/password_reset_done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}),
#  (r'^accounts/password_change/$', password_change, {'template_name': 'registration/password_change.html'}),
#  (r'^accounts/password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),
#)
