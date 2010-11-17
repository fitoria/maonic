# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import *

class MaonicAdmin(admin.ModelAdmin):
    def queryset(self, request):
        if request.user.is_superuser:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(user=request.user)

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
