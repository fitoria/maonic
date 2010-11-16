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

    def __unicode__(self):
        return self.nombre

    class Meta:
        abstract = True

class Familia(FichaBase):
    nombre_finca = models.CharField('Nombre de finca', max_length=50)
    area_finca = models.DecimalField('Area de la finca en Manzanas', 
            decimal_places=2, max_digits=8)

    def __unicode__(self):
        return '%s - %s' % (self.nombre_finca, self.nombre)

class Cooperativa(FichaBase):
    fecha_est = models.DateField('fecha de establecimiento')
    representante_legal = models.CharField(max_length=100)
    representante_tecnico = models.CharField(max_length=100)
    num_hombres = models.IntegerField('numero de miembros hombres')
    num_mujeres = models.IntegerField('numero de miembros mujeres')
    
class Centrales(FichaBase):
    fecha_est = models.DateField('fecha de establecimiento')
    representante_legal = models.CharField(max_length=100)
    representante_tecnico = models.CharField(max_length=100)
    num_asociaciones = models.IntegerField('numero de asociaciones agrupadas:')
    num_cooperativas= models.IntegerField('numero de asociaciones agrupadas:')
    num_hombres = models.IntegerField('numero de miembros hombres')
    num_mujeres = models.IntegerField('numero de miembros mujeres')

class AsistenciaTecnica(FichaBase):
    desde= models.IntegerField('desde cuando provee asistencia')
    promedio = models.IntegerField('promedio de fincas atendidas por ano')

class OrgAcompanante(FichaBase):
    pass

class ComInsumo(FichaBase):
    desde_insumo = models.IntegerField('desde cuando provee insumo')
    promedio = models.IntegerField('promedio de clientes')

class ComProducto(FichaBase):
    desde = models.IntegerField('desde cuando comercializa')
    promedio = models.DecimalField('promedio de volumen de negocio en US$ por ano', 
            decimal_places=2, max_digits=8)

class Certificadora(FichaBase):
    desde = models.IntegerField('desde cuando certifican')
    promedio = models.IntegerField('promedio de certificaciones')

class Financiera(FichaBase):
    desde = models.IntegerField('desde cuando certifican')
    promedio = models.IntegerField('promedio de certificaciones')
    #proveen financiamiento para?

class OrgPublica(FichaBase):
    representante_legal = models.CharField(max_length=100)
    representante_tecnico = models.CharField(max_length=100)
