from django.db import models
from lugar.models import Municipio

class FichaBase(models.Model):
    nombre = models.CharField('Nombre', max_length=150)
    municipio = models.ForeignKey(Municipio)
    lat = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='latitud')
    lon = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='longitud')

    class Meta:
        proxy = True

class Cooperativa(FichaBase):
    pass

class Centrales(FichaBase):
    pass

class AsistenciaTecnica(FichaBase):
    pass

class OrgAcompanante(FichaBase):
    pass

class ComInsumo(FichaBase):
    pass

class ComProducto(FichaBase):
    pass

class Certificadora(FichaBase):
    pass

class Financiera(FichaBase):
    pass

class OrgPublica(FichaBase):
    pass
