# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import session_required
from django.template import RequestContext
from forms import FilterForm 

model_dict = {
    'familia': Familia,
    'cooperativa': Cooperativa,
    'centrales': Centrales,
    'asistencia': AsistenciaTecnica,
    'insumo': ComInsumo,
    'producto': ComProducto,
    'certificadora': Certificadora,
    'financiera': Financiera,
    'orgpublica': OrgPublica,
    }

def index(request):
    pass

@session_required
def obtener_lista_paginada(request, modelo):
    '''Vista ajax para obtener lista de elementos en 
    la vista luego del filtrado, modelo es una cadena
    definida dentro del diccionario model_dict en las 
    primeras lineas de este archivo
    '''
    if request.is_ajax():
        lista_objetos = model_dict[modelo].objects.all()
        paginator = Paginator(lista_objetos, 25)

        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            objetos = paginator.page(page)
        except  (EmptyPage, InvalidPage):
            objetos = paginator.page(paginator.num_pages)

        #se le agrega el tipo de modelo para construir la url
        lista_objetos = [dict(objeto, modelo = modelo) for objeto 
                in objectos.object_list().values('id', 'nombre')]
        return HttpResponse(simplejson.dumps(lista_objetos), mimetype="application/json")

def obtener_lista(request, modelo):
    #TODO: agregr request.ajax
    lista = []
    params = _get_params(request.session)
    for objeto in model_dict[modelo].objects.filter(**params):
        if objeto.lat and objeto.lon:
            dicc = dict(nombre=objeto.nombre, id=objeto.id, 
                        lon=foat(objeto.lon) , lat=float(objeto.lat),
                        modelo= modelo)
        else:
            dicc = dict(nombre=objeto.nombre, id=objeto.id, 
                        lon=float(objeto.municipio.longitud) , 
                        lat=float(objeto.municipio.latitud),
                        modelo= modelo)
        lista.append(dicc)

    serializado = simplejson.dumps(lista)
    return HttpResponse(serializado, mimetype='application/json')

def formulario(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            lista_modelos = [] #ojala fueran chavalas y no tablas :-(
            for key in model_dict.keys():
                if form.cleaned_data[key] == 'on':
                    lista_modelos.append(key)
            
            request.session['lista_modelos'] = lista_modelos
            #validar aca!

            #aburriiiiiiiiiido 
            for coso in ('semillas', 'materia_procesada', 'buenas_practicas', 
                    'arboles', 'cultivos', 'animales',
                    'tipo_organizacion', 'certificacion', 'area_trabajo'):
                request.session[coso] = form.cleaned_data[coso]
            #TODO:hacer un flash al estilo rails redigirir a mapita
            request.session['activo'] = True
            return HttpResponseRedirect('/mapeo/mapa') 
    else:
        form = FilterForm()

    return render_to_response('mapeo/formulario.html', 
            {'form': form},
            context_instance=RequestContext(request))


def _get_params(session):
    '''funcion interna para devolver parametros 
    del formulario de busqueda'''
    keys = ('semillas', 'materia_procesada', 'buenas_practicas', 
            'arboles', 'cultivos', 'animales',
            'tipo_organizacion', 'certificacion', 'area_trabajo')
    params = {}
    for key in keys:
        param_key = key + '__in'
        if session[key] != []:
            params[param_key] = session[key] 

    return params
    
@session_required
def mapa(request):
    return render_to_response('mapeo/mapa.html', 
            {'lista_modelos': request.session['lista_modelos']},
            context_instance=RequestContext(request))
