import os
from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('mapeo.views',
    (r'^lista/(?P<modelo>\w+)/$', 'obtener_lista'),
    (r'^formulario/$', 'formulario'),
)
