# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from lugar.models import Municipio

class SelectorBase(models.Model):
    '''modelo abstracto para semilla, materia, 
    buenas practicas, organizacion, certificacion'''
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        abstract = True 

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
            decimal_places=2, verbose_name='latitud')
    lon = models.DecimalField(blank=True, max_digits=8, 
            decimal_places=2, verbose_name='longitud')
    telefono = models.CharField(max_length=8, blank=True, null=True) 
    celular = models.CharField(max_length=8, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True)
    pagina_web = models.URLField(blank=True, null=True)
    #campos de control y seguridad
    user = models.ForeignKey(User) #usuario que lo creo
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now=True)

    #rubros genericos que estan en todos lados
    arboles = models.ManyToManyField(RubroArboles)
    animales = models.ManyToManyField(RubroAnimales)
    cultivos = models.ManyToManyField(RubroCultivo)
    semillas = models.ManyToManyField(Semilla)
    materia_procesada = models.ManyToManyField(MateriaProcesada)
    certificacion = models.ManyToManyField(Certificacion)
    buenas_practicas = models.ManyToManyField(BuenasPracticas)


    def __unicode__(self):
        return self.nombre

    class Meta:
        abstract = True

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
    num_asociaciones = models.IntegerField('numero de asociaciones agrupadas:')
    num_cooperativas= models.IntegerField('numero de asociaciones agrupadas:')
    num_hombres = models.IntegerField('numero de miembros hombres')
    num_mujeres = models.IntegerField('numero de miembros mujeres')
    area_trabajo = models.ManyToManyField(AreaTrabajo)

class AsistenciaTecnica(FichaBase):
    desde= models.IntegerField('desde cuando provee asistencia')
    promedio = models.IntegerField('promedio de fincas atendidas por ano')
    tipo_org = models.ManyToManyField(TipoOrganizacion)

class ComInsumo(FichaBase):
    desde_insumo = models.IntegerField('desde cuando provee insumo')
    promedio = models.IntegerField('promedio de clientes')
    tipo_cliente = models.ManyToManyField(TipoOrganizacion)

class ComProducto(FichaBase):
    desde = models.IntegerField('desde cuando comercializa')
    promedio = models.DecimalField('promedio de volumen de negocio en US$ por ano', 
            decimal_places=2, max_digits=8)
    tipo_prov = models.ManyToManyField(TipoOrganizacion)

class Certificadora(FichaBase):
    desde = models.IntegerField('desde cuando certifican')
    promedio = models.IntegerField('promedio de certificaciones')
    tipo_cliente = models.ManyToManyField(TipoOrganizacion)

class Financiera(FichaBase):
    desde = models.IntegerField('desde cuando certifican')
    promedio = models.IntegerField('promedio de certificaciones')
    tipo_cliente = models.ManyToManyField(TipoOrganizacion)

class OrgPublica(FichaBase):
    representante_legal = models.CharField(max_length=100)
    representante_tecnico = models.CharField(max_length=100)
    area_trabajo = models.ManyToManyField(AreaTrabajo)

#tipo de usuario add to class, para filtrar admin.
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.nombre

User.add_to_class('tipo', models.ManyToManyField(TipoUsuario))
