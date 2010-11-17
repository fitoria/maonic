# -*- coding: UTF-8 -*-
from django import forms
from models import *

class FilterForm(forms.Form):
    #columna de la izq
    familia = forms.CharField(label='Familia', 
            widget = forms.CheckboxInput)
    cooperativa = forms.CharField(label='Cooperativa', 
            widget = forms.CheckboxInput)
    centrales = forms.CharField(label='Centrales', 
            widget = forms.CheckboxInput)
    asistencia = forms.CharField(label='Asistencia', 
            widget = forms.CheckboxInput)
    insumo = forms.CharField(label='Empresa comercializadora de Insumos', 
            widget = forms.CheckboxInput)
    producto = forms.CharField(label='Empresa comercializadora producto.', 
            widget = forms.CheckboxInput)
    certificadora = forms.CharField(label='Empresa certificadora', 
            widget = forms.CheckboxInput)
    financiera = forms.CharField(label='Empresa Financiera', 
            widget = forms.CheckboxInput)
    orgpublica = forms.CharField(label='Organización Pública', 
            widget = forms.CheckboxInput)

    #rubros
    rubro_cultivo = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroCultivo.objects.all(), label='Rubro Cultivo', 
            required=False)
    rubro_animales = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroArboles.objects.all(), label='Rubro Animales', 
            required=False)
    rubro_arboles = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=RubroAnimales.objects.all(), label='Rubro Arboles',
            required=False)

    #otros filtros
    semilla = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=Semilla.objects.all(), label='Semilla',
            required=False)
    materia_procesada = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=MateriaProcesada.objects.all(), label='Materia Procesada', 
            required=False)
    buenas_practicas = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=BuenasPracticas.objects.all(), label='Buenas prácticas',
            required=False)
    tipo_organizacion = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=TipoOrganizacion.objects.all(), label='Tipo organización',
            required=False)
    certificacion = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=Certificacion.objects.all(), label='Certificación', 
            required=False)
    area_trabajo= forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,
            queryset=AreaTrabajo.objects.all(), label='Area de trabajo', 
            required=False)
