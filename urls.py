from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^mapeo/', include('maonic.mapeo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
)

urlpatterns += patterns('',
  (r'^accounts/profile/$', direct_to_template, {'template': 'registration/profile.html'}),
  (r'^accounts/password_reset/$', password_reset, {'template_name': 'registration/password_reset.html'}),
  (r'^accounts/password_reset_done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}),
  (r'^accounts/password_change/$', password_change, {'template_name': 'registration/password_change.html'}),
  (r'^accounts/password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),
)
