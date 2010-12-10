# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from decorators import session_required
from django.template import RequestContext
from django.core.exceptions import ViewDoesNotExist, ValidationError
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

@session_required
def obtener_lista_paginada(request, modelo):
    '''Vista ajax para obtener lista de elementos en 
    la vista luego del filtrado, modelo es una cadena
    definida dentro del diccionario model_dict en las 
    primeras lineas de este archivo
    '''
    if request.is_ajax():
        params = _get_params(request.session)
        lista_objetos = _get_model(modelo, request.session).objects.filter(**params).distinct()
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
                in objetos.object_list.values('id', 'nombre')]
        resultados = dict(enlaces = lista_objetos, 
                          sig = objetos.next_page_number(), 
                          ant = objetos.previous_page_number())
        return HttpResponse(simplejson.dumps(resultados), mimetype="application/json")

@session_required
def obtener_lista(request, modelo):
    if request.is_ajax():
        lista = []
        params = _get_params(request.session)
        for objeto in _get_model(modelo).objects.filter(**params):
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

def _get_model(model, session=None):
    if model in model_dict:
        if session:
            if model in session['lista_modelos']:
                return model_dict[model]
            else:
                raise ValidationError('Modelo no esta en sesion')
        else:
            return model_dict[model]

    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not defined in VALID_VIEWS." % (vista, 'encuesta.views'))

@session_required
def mapa(request):
    return render_to_response('mapeo/mapa.html', 
            {'lista_modelos': request.session['lista_modelos']},
            context_instance=RequestContext(request))

def ficha(request, modelo, id):
    '''Retorna ficha, plantillas cargadas dinamicamente'''
    objeto = get_object_or_404(_get_model(modelo), id=id)
    template_name = 'mapeo/ficha_%s.html' % modelo
    return render_to_response(template_name, {'objeto': objeto},
            context_instance=RequestContext(request))

def galeria(request, modelo, id):
    '''Retorna vista a galeria de fotos'''
    objeto = get_object_or_404(_get_model(modelo), id=id)
    return render_to_response('mapeo/galeria.html', {'objeto': objeto},
            context_instance=RequestContext(request))

@session_required
def lista(request):
    lista_modelos = request.session['lista_modelos']
    params = _get_params(request.session)
    dicc = {'lista_modelos': lista_modelos,
        'familia': 0,
        'cooperativa': 0,
        'centrales': 0,
        'asistencia': 0,
        'insumo': 0,
        'producto': 0,
        'certificadora': 0,
        'financiera': 0,
        'orgpublica': 0,
    }
    for modelo in lista_modelos:
        dicc[modelo] = _get_model(modelo).objects.filter(**params).distinct().count() 

    return render_to_response('mapeo/lista.html', 
            dicc,
            context_instance=RequestContext(request))
