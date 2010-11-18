import os
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

urlpatterns = patterns('maonic.mapeo.views',
    (r'^$', direct_to_template, {'template': 'mapeo/index.html'}),
    (r'^resultados/$', direct_to_template, {'template': 'mapeo/resultados.html'}),

    (r'^lista/$', direct_to_template, {'template': 'mapeo/lista.html'}),
    (r'^lista/(?P<modelo>\w+)/$', 'obtener_lista_paginada'),
    (r'^formulario/$', 'formulario'),
    (r'^mapa/$', 'mapa'),
    (r'^mapa/(?P<modelo>\w+)/$', 'obtener_lista'),
)
