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

def lista_actores(request):
    '''Lista general de todos los actores'''
#@session_required TODO hacer el método que guarde la sesion
def obtener_lista(request, modelo):
    '''Vista ajax para obtener lista de elementos en 
    la vista luego del filtrado, modelo es una cadena
    definida dentro del diccionario model_dict en las 
    primeras lineas de este archivo
    '''
    if request.is_ajax():
        lista_objetos = model_dict['modelo'].objects.all()
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

def formulario(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            lista_modelos = [] #ojala fueran chavalas y no tablas :-(
            for key in model_dict.keys():
                if form.cleaned_data[key] is 'on':
                    lista_modelos.append(key)
            
            request.session['lista_modelos'] = lista_modelos

            #aburriiiiiiiiiido 
            for coso in ('semilla', 'materia_procesada', 'buenas_practicas', 
                    'tipo_organizacion', 'certificacion', 'area_trabajo'):
                request.session[coso] = form.cleaned_data[coso]
            #TODO:hacer un flash al estilo rails redigirir a mapita
            return HttpResponseRedirect('/mapeo/mapa') 
    else:
        form = FilterForm()

    return render_to_response('mapeo/formulario.html', 
            {'form': form},
            context_instance=RequestContext(request))
