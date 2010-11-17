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

    def get_form(self, request, obj=None, ** kwargs):
        if request.user.is_superuser:
            form = super(EncuestaAdmin, self).get_form(self, request, ** kwargs)
        else:
            form = super(EncuestaAdmin, self).get_form(self, request, ** kwargs)
            form.base_fields['user'].queryset = User.objects.filter(pk=request.user.pk)
        return form

admin.site.register(Familia, MaonicAdmin)
admin.site.register(Cooperativa, MaonicAdmin)
admin.site.register(Centrales, MaonicAdmin)
admin.site.register(AsistenciaTecnica, MaonicAdmin)
admin.site.register(ComInsumo, MaonicAdmin)
admin.site.register(ComProducto, MaonicAdmin)
admin.site.register(Certificadora, MaonicAdmin)
admin.site.register(Financiera, MaonicAdmin)
admin.site.register(OrgPublica, MaonicAdmin)
admin.site.register(RubroCultivo)
admin.site.register(RubroArboles)
admin.site.register(RubroAnimales)
admin.site.register(Semilla)
admin.site.register(MateriaProcesada)
admin.site.register(BuenasPracticas)
admin.site.register(TipoOrganizacion)
admin.site.register(AreaTrabajo)
admin.site.register(TipoUsuario)
