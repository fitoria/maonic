# -*- coding: UTF-8 -*-
from django import forms
from models import *

class FilterForm(forms.Form):
    #columna de la izq
    familia = forms.CharField(initial='familia', label='Familia', 
            widget = forms.CheckboxInput)
    cooperativa = forms.CharField(initial='cooperativa', label='Cooperativa', 
            widget = forms.CheckboxInput)
    centrales = forms.CharField(initial='centrales', label='Centrales', 
            widget = forms.CheckboxInput)
    asistencia = forms.CharField(initial='asistencia', label='Asistencia', 
            widget = forms.CheckboxInput)
    insumo = forms.CharField(initial='insumo', label='Empresa comercializadora de Insumos', 
            widget = forms.CheckboxInput)
    producto = forms.CharField(initial='producto', label='Empresa comercializadora producto.', 
            widget = forms.CheckboxInput)
    certificadora = forms.CharField(initial='certificadora', label='Empresa certificadora', 
            widget = forms.CheckboxInput)
    financiera = forms.CharField(initial='financiera', label='Empresa Financiera', 
            widget = forms.CheckboxInput)
    orgpublica = forms.CharField(initial='orgpublica', label='Organización Pública', 
            widget = forms.CheckboxInput)

    #rubros
    rubro_cultivo = forms.MultipleChoiceField(widget=forms.SelectMultiple,
            choices=RubroCultivo.objects.all(), label='Rubro Cultivo')
    rubro_animales = forms.MultipleChoiceField(widget=forms.SelectMultiple,
            choices=RubroArboles.objects.all(), label='Rubro Animales')
    rubro_arboles = forms.MultipleChoiceField(widget=forms.SelectMultiple,
            choices=RubroAnimales.objects.all(), label='Rubro Arboles')

    #otros filtros
    semilla = forms.MultipleChoiceField(widget=forms.SelectMultiple,
            choices=Semilla.objects.all(), label='Semilla')
    materia_procesada = forms.MultipleChoiceField(widget=forms.SelectMultiple,
            choices=MateriaProcesada.objects.all(), label='Materia Procesada')
    buenas_practicas = forms.MultipleChoiceField(widget=forms.SelectMultiple,
            choices=BuenasPracticas.objects.all(), label='Buenas prácticas')
    tipo_organizacion = forms.MultipleChoiceField(widget=forms.SelectMultiple,
            choices=TipoOrganizacion.objects.all(), label='Tipo organización')
    certificacion = forms.MultipleChoiceField(widget=forms.SelectMultiple,
            choices=Certificacion.objects.all(), label='Certificación')
    area_trabajo= forms.MultipleChoiceField(widget=forms.SelectMultiple,
            choices=AreaTrabajo.objects.all(), label='Area de trabajo')
