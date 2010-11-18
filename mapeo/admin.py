# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from models import *

class MaonicAdmin(admin.ModelAdmin):
    def queryset(self, request):
        if request.user.is_superuser:
            return self.model.objects.all()
        elif request.user.is_staff:
            return self.model.objects.filter(user=request.user)
    filter_horizontal = ('arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')

class FamiliaAdmin(MaonicAdmin):
    filter_horizontal = ('tipo_org','arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')

class CooperativaAdmin(MaonicAdmin):
    filter_horizontal = ('area_trabajo','arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')

class CentralesAdmin(MaonicAdmin):
    filter_horizontal = ('area_trabajo','arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')

class AsistenciaTecnicaAdmin(MaonicAdmin):
    filter_horizontal = ('tipo_org','arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')

class ComInsumoAdmin(MaonicAdmin):
    filter_horizontal = ('tipo_cliente','arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')

class ComProductoAdmin(MaonicAdmin):
    filter_horizontal = ('tipo_prov','arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')

class CertificadoraAdmin(MaonicAdmin):
    filter_horizontal = ('tipo_cliente','arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')

class FinancieraAdmin(MaonicAdmin):
    filter_horizontal = ('tipo_cliente','arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')

class OrgPublicaAdmin(MaonicAdmin):
    filter_horizontal = ('area_trabajo','arboles','animales','cultivos','semillas','materia_procesada','certificacion','buenas_practicas')
    
    #def get_form(self, request, obj=None, ** kwargs):
    #    if request.user.is_superuser:
    #        form = super(MaonicAdmin, self).get_form(self, request, ** kwargs)
    #    else:
    #        form = super(MaonicAdmin, self).get_form(self, request, ** kwargs)
    #        form.base_fields['user'].queryset = User.objects.filter(pk=request.user.pk)
    #    return form
#admin.site.register(Familia, MaonicAdmin)
admin.site.register(Familia,FamiliaAdmin)

#admin.site.register(Cooperativa, MaonicAdmin)
admin.site.register(Cooperativa,CooperativaAdmin)

#admin.site.register(Centrales, MaonicAdmin)
admin.site.register(Centrales,CentralesAdmin)

#admin.site.register(AsistenciaTecnica, MaonicAdmin)
admin.site.register(AsistenciaTecnica,AsistenciaTecnicaAdmin)

#admin.site.register(ComInsumo, MaonicAdmin)
admin.site.register(ComInsumo,ComInsumoAdmin)

#admin.site.register(ComProducto, MaonicAdmin)
admin.site.register(ComProducto,ComProductoAdmin)

#admin.site.register(Certificadora, MaonicAdmin)
admin.site.register(Certificadora,CertificadoraAdmin)

#admin.site.register(Financiera, MaonicAdmin)
admin.site.register(Financiera,FinancieraAdmin)

#admin.site.register(OrgPublica, MaonicAdmin)
admin.site.register(OrgPublica,OrgPublicaAdmin)

admin.site.register(RubroCultivo)
admin.site.register(RubroArboles)
admin.site.register(RubroAnimales)
admin.site.register(Semilla)
admin.site.register(MateriaProcesada)
admin.site.register(BuenasPracticas)
admin.site.register(TipoOrganizacion)
admin.site.register(AreaTrabajo)
