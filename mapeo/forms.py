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
    rubro_cultivo = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroCultivo.objects.all(), label='Rubro Cultivo')
    rubro_animales = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroArboles.objects.all(), label='Rubro Animales')
    rubro_arboles = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroAnimales.objects.all(), label='Rubro Arboles')

    #otros filtros
    semilla = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=Semilla.objects.all(), label='Semilla')
    materia_procesada = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=MateriaProcesada.objects.all(), label='Materia Procesada')
    buenas_practicas = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=BuenasPracticas.objects.all(), label='Buenas prácticas')
    tipo_organizacion = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=TipoOrganizacion.objects.all(), label='Tipo organización')
    certificacion = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=Certificacion.objects.all(), label='Certificación')
    area_trabajo= forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=AreaTrabajo.objects.all(), label='Area de trabajo')
