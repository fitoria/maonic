# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from lugar.models import Municipio
from thumbs import ImageWithThumbsField
#Galeria de foto.
FOTOS_SIZES = ((640, 480), (227, 154))

#class Galeria(models.Model):
#    '''Modelo de galeria de foto, solo se permite 5 fotos'''
#    nombre = models.CharField(max_length=140)
#    user = models.ForeignKey(User)
#    foto1 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/') 
#    foto2 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
#    foto3 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
#    foto4 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
#    foto5 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
#
#    def __unicode__(self):
#        return self.nombre
#    
#    def get_thumb(self):
#        return self.foto1.url_227x154

class SelectorBase(models.Model):
    '''modelo abstracto para semilla, materia, 
    buenas practicas, organizacion, certificacion'''
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        abstract = True
        ordering = ['nombre'] 

class RubroCultivo(SelectorBase):
    pass

class RubroArboles(SelectorBase):
    pass

class RubroAnimales(SelectorBase):
    pass

class Semilla(SelectorBase):
    pass

class MateriaProcesada(SelectorBase):
    pass

class BuenasPracticas(SelectorBase):
    pass

class TipoOrganizacion(SelectorBase):
    pass

class Certificacion(SelectorBase):
    pass

class AreaTrabajo(SelectorBase):
    pass

class FichaBase(models.Model):
    '''Modelo abstracto para la creacion de fichas'''
    nombre = models.CharField('Nombre', max_length=150)
    direccion = models.TextField()
    municipio = models.ForeignKey(Municipio)
    lat = models.DecimalField(blank=True, max_digits=8, 
            decimal_places=2, verbose_name='latitud', null=True)
    lon = models.DecimalField(blank=True, max_digits=8, 
            decimal_places=2, verbose_name='longitud', null=True)
    telefono = models.CharField(max_length=8, blank=True, null=True) 
    celular = models.CharField(max_length=8, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True)
    pagina_web = models.URLField(blank=True, null=True)
    #campos de control y seguridad
    user = models.ForeignKey(User) #usuario que lo creo
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now=True)

    #rubros genericos que estan en todos lados
    arboles = models.ManyToManyField(RubroArboles, blank=True)
    animales = models.ManyToManyField(RubroAnimales, blank=True)
    cultivos = models.ManyToManyField(RubroCultivo, blank=True)
    semillas = models.ManyToManyField(Semilla, blank=True)
    materia_procesada = models.ManyToManyField(MateriaProcesada, blank=True)
    certificacion = models.ManyToManyField(Certificacion, blank=True)
    buenas_practicas = models.ManyToManyField(BuenasPracticas, blank=True)

    #Fotos
    foto1 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
    foto2 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
    foto3 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
    foto4 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 
    foto5 = ImageWithThumbsField(sizes = FOTOS_SIZES, upload_to = 'galeria/', blank=True, null=True) 

    def __unicode__(self):
        return self.nombre

    class Meta:
        abstract = True
        ordering = ['nombre']

class Familia(FichaBase):
    nombre_finca = models.CharField('Nombre de finca', max_length=50)
    area_finca = models.DecimalField('Area de la finca en Manzanas', 
            decimal_places=2, max_digits=8)
    tipo_org = models.ManyToManyField(TipoOrganizacion)

    def __unicode__(self):
        return '%s - %s' % (self.nombre_finca, self.nombre)

class Cooperativa(FichaBase):
    fecha_est = models.DateField('fecha de establecimiento')
    representante_legal = models.CharField(max_length=100)
    representante_tecnico = models.CharField(max_length=100)
    num_hombres = models.IntegerField('numero de miembros hombres')
    num_mujeres = models.IntegerField('numero de miembros mujeres')
    area_trabajo = models.ManyToManyField(AreaTrabajo)
    
class Centrales(FichaBase):
    fecha_est = models.DateField('fecha de establecimiento')
    representante_legal = models.CharField(max_length=100)
    representante_tecnico = models.CharField(max_length=100)
    num_asociaciones = models.IntegerField('numero de asociaciones agrupadas')
    num_cooperativas= models.IntegerField('numero de cooperativas agrupadas')
    num_hombres = models.IntegerField('numero de miembros hombres')
    num_mujeres = models.IntegerField('numero de miembros mujeres')
    area_trabajo = models.ManyToManyField(AreaTrabajo)

    class Meta:
        verbose_name_plural = 'centrales'
        verbose_name = 'central'

class AsistenciaTecnica(FichaBase):
    desde= models.IntegerField('desde cuando provee asistencia')
    promedio = models.IntegerField('promedio de fincas atendidas por año')
    tipo_org = models.ManyToManyField(TipoOrganizacion)

    class Meta:
        verbose_name_plural = 'Agentes de asistencia técnica'
        verbose_name = 'Agente de asistencia técnica'

class ComInsumo(FichaBase):
    desde_insumo = models.IntegerField('desde cuando provee insumo')
    promedio = models.IntegerField('promedio de clientes')
    tipo_cliente = models.ManyToManyField(TipoOrganizacion)

    class Meta:
        verbose_name_plural = 'Empresas comercializadora de insumos'
        verbose_name = 'Empresa comercializadora de insumos'

class ComProducto(FichaBase):
    desde = models.IntegerField('desde cuando comercializa')
    promedio = models.DecimalField('promedio de volumen de negocio en US$ por año', 
            decimal_places=2, max_digits=8)
    tipo_prov = models.ManyToManyField(TipoOrganizacion)

    class Meta:
        verbose_name_plural = 'Empresas comercializadora de productos'
        verbose_name = 'Empresa comercializadora de productos'

class Certificadora(FichaBase):
    desde = models.IntegerField('desde cuando certifican')
    promedio = models.IntegerField('promedio de certificaciones')
    tipo_cliente = models.ManyToManyField(TipoOrganizacion)

    class Meta:
        verbose_name_plural = 'Empresas certificadora'
        verbose_name = 'Empresa certificadora'

class Financiera(FichaBase):
    desde = models.IntegerField('desde cuando certifican')
    promedio = models.IntegerField('promedio de certificaciones')
    tipo_cliente = models.ManyToManyField(TipoOrganizacion)

class OrgPublica(FichaBase):
    representante_legal = models.CharField(max_length=100)
    representante_tecnico = models.CharField(max_length=100)
    area_trabajo = models.ManyToManyField(AreaTrabajo)

    class Meta:
        verbose_name_plural = 'Organizaciones Pública'
        verbose_name = 'Organización Pública'
