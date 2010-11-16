# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field arboles on 'Financiera'
        db.create_table('mapeo_financiera_arboles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('financiera', models.ForeignKey(orm['mapeo.financiera'], null=False)),
            ('rubroarboles', models.ForeignKey(orm['mapeo.rubroarboles'], null=False))
        ))
        db.create_unique('mapeo_financiera_arboles', ['financiera_id', 'rubroarboles_id'])

        # Adding M2M table for field animales on 'Financiera'
        db.create_table('mapeo_financiera_animales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('financiera', models.ForeignKey(orm['mapeo.financiera'], null=False)),
            ('rubroanimales', models.ForeignKey(orm['mapeo.rubroanimales'], null=False))
        ))
        db.create_unique('mapeo_financiera_animales', ['financiera_id', 'rubroanimales_id'])

        # Adding M2M table for field cultivos on 'Financiera'
        db.create_table('mapeo_financiera_cultivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('financiera', models.ForeignKey(orm['mapeo.financiera'], null=False)),
            ('rubrocultivo', models.ForeignKey(orm['mapeo.rubrocultivo'], null=False))
        ))
        db.create_unique('mapeo_financiera_cultivos', ['financiera_id', 'rubrocultivo_id'])

        # Adding M2M table for field semillas on 'Financiera'
        db.create_table('mapeo_financiera_semillas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('financiera', models.ForeignKey(orm['mapeo.financiera'], null=False)),
            ('semilla', models.ForeignKey(orm['mapeo.semilla'], null=False))
        ))
        db.create_unique('mapeo_financiera_semillas', ['financiera_id', 'semilla_id'])

        # Adding M2M table for field materia_procesada on 'Financiera'
        db.create_table('mapeo_financiera_materia_procesada', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('financiera', models.ForeignKey(orm['mapeo.financiera'], null=False)),
            ('materiaprocesada', models.ForeignKey(orm['mapeo.materiaprocesada'], null=False))
        ))
        db.create_unique('mapeo_financiera_materia_procesada', ['financiera_id', 'materiaprocesada_id'])

        # Adding M2M table for field certificacion on 'Financiera'
        db.create_table('mapeo_financiera_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('financiera', models.ForeignKey(orm['mapeo.financiera'], null=False)),
            ('certificacion', models.ForeignKey(orm['mapeo.certificacion'], null=False))
        ))
        db.create_unique('mapeo_financiera_certificacion', ['financiera_id', 'certificacion_id'])

        # Adding M2M table for field tipo_cliente on 'Financiera'
        db.create_table('mapeo_financiera_tipo_cliente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('financiera', models.ForeignKey(orm['mapeo.financiera'], null=False)),
            ('tipoorganizacion', models.ForeignKey(orm['mapeo.tipoorganizacion'], null=False))
        ))
        db.create_unique('mapeo_financiera_tipo_cliente', ['financiera_id', 'tipoorganizacion_id'])

        # Adding M2M table for field arboles on 'OrgAcompanante'
        db.create_table('mapeo_orgacompanante_arboles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgacompanante', models.ForeignKey(orm['mapeo.orgacompanante'], null=False)),
            ('rubroarboles', models.ForeignKey(orm['mapeo.rubroarboles'], null=False))
        ))
        db.create_unique('mapeo_orgacompanante_arboles', ['orgacompanante_id', 'rubroarboles_id'])

        # Adding M2M table for field animales on 'OrgAcompanante'
        db.create_table('mapeo_orgacompanante_animales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgacompanante', models.ForeignKey(orm['mapeo.orgacompanante'], null=False)),
            ('rubroanimales', models.ForeignKey(orm['mapeo.rubroanimales'], null=False))
        ))
        db.create_unique('mapeo_orgacompanante_animales', ['orgacompanante_id', 'rubroanimales_id'])

        # Adding M2M table for field cultivos on 'OrgAcompanante'
        db.create_table('mapeo_orgacompanante_cultivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgacompanante', models.ForeignKey(orm['mapeo.orgacompanante'], null=False)),
            ('rubrocultivo', models.ForeignKey(orm['mapeo.rubrocultivo'], null=False))
        ))
        db.create_unique('mapeo_orgacompanante_cultivos', ['orgacompanante_id', 'rubrocultivo_id'])

        # Adding M2M table for field semillas on 'OrgAcompanante'
        db.create_table('mapeo_orgacompanante_semillas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgacompanante', models.ForeignKey(orm['mapeo.orgacompanante'], null=False)),
            ('semilla', models.ForeignKey(orm['mapeo.semilla'], null=False))
        ))
        db.create_unique('mapeo_orgacompanante_semillas', ['orgacompanante_id', 'semilla_id'])

        # Adding M2M table for field materia_procesada on 'OrgAcompanante'
        db.create_table('mapeo_orgacompanante_materia_procesada', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgacompanante', models.ForeignKey(orm['mapeo.orgacompanante'], null=False)),
            ('materiaprocesada', models.ForeignKey(orm['mapeo.materiaprocesada'], null=False))
        ))
        db.create_unique('mapeo_orgacompanante_materia_procesada', ['orgacompanante_id', 'materiaprocesada_id'])

        # Adding M2M table for field certificacion on 'OrgAcompanante'
        db.create_table('mapeo_orgacompanante_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgacompanante', models.ForeignKey(orm['mapeo.orgacompanante'], null=False)),
            ('certificacion', models.ForeignKey(orm['mapeo.certificacion'], null=False))
        ))
        db.create_unique('mapeo_orgacompanante_certificacion', ['orgacompanante_id', 'certificacion_id'])

        # Adding M2M table for field arboles on 'Centrales'
        db.create_table('mapeo_centrales_arboles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centrales', models.ForeignKey(orm['mapeo.centrales'], null=False)),
            ('rubroarboles', models.ForeignKey(orm['mapeo.rubroarboles'], null=False))
        ))
        db.create_unique('mapeo_centrales_arboles', ['centrales_id', 'rubroarboles_id'])

        # Adding M2M table for field animales on 'Centrales'
        db.create_table('mapeo_centrales_animales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centrales', models.ForeignKey(orm['mapeo.centrales'], null=False)),
            ('rubroanimales', models.ForeignKey(orm['mapeo.rubroanimales'], null=False))
        ))
        db.create_unique('mapeo_centrales_animales', ['centrales_id', 'rubroanimales_id'])

        # Adding M2M table for field cultivos on 'Centrales'
        db.create_table('mapeo_centrales_cultivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centrales', models.ForeignKey(orm['mapeo.centrales'], null=False)),
            ('rubrocultivo', models.ForeignKey(orm['mapeo.rubrocultivo'], null=False))
        ))
        db.create_unique('mapeo_centrales_cultivos', ['centrales_id', 'rubrocultivo_id'])

        # Adding M2M table for field semillas on 'Centrales'
        db.create_table('mapeo_centrales_semillas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centrales', models.ForeignKey(orm['mapeo.centrales'], null=False)),
            ('semilla', models.ForeignKey(orm['mapeo.semilla'], null=False))
        ))
        db.create_unique('mapeo_centrales_semillas', ['centrales_id', 'semilla_id'])

        # Adding M2M table for field materia_procesada on 'Centrales'
        db.create_table('mapeo_centrales_materia_procesada', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centrales', models.ForeignKey(orm['mapeo.centrales'], null=False)),
            ('materiaprocesada', models.ForeignKey(orm['mapeo.materiaprocesada'], null=False))
        ))
        db.create_unique('mapeo_centrales_materia_procesada', ['centrales_id', 'materiaprocesada_id'])

        # Adding M2M table for field certificacion on 'Centrales'
        db.create_table('mapeo_centrales_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centrales', models.ForeignKey(orm['mapeo.centrales'], null=False)),
            ('certificacion', models.ForeignKey(orm['mapeo.certificacion'], null=False))
        ))
        db.create_unique('mapeo_centrales_certificacion', ['centrales_id', 'certificacion_id'])

        # Adding M2M table for field area_trabajo on 'Centrales'
        db.create_table('mapeo_centrales_area_trabajo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centrales', models.ForeignKey(orm['mapeo.centrales'], null=False)),
            ('areatrabajo', models.ForeignKey(orm['mapeo.areatrabajo'], null=False))
        ))
        db.create_unique('mapeo_centrales_area_trabajo', ['centrales_id', 'areatrabajo_id'])

        # Adding M2M table for field arboles on 'AsistenciaTecnica'
        db.create_table('mapeo_asistenciatecnica_arboles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('asistenciatecnica', models.ForeignKey(orm['mapeo.asistenciatecnica'], null=False)),
            ('rubroarboles', models.ForeignKey(orm['mapeo.rubroarboles'], null=False))
        ))
        db.create_unique('mapeo_asistenciatecnica_arboles', ['asistenciatecnica_id', 'rubroarboles_id'])

        # Adding M2M table for field animales on 'AsistenciaTecnica'
        db.create_table('mapeo_asistenciatecnica_animales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('asistenciatecnica', models.ForeignKey(orm['mapeo.asistenciatecnica'], null=False)),
            ('rubroanimales', models.ForeignKey(orm['mapeo.rubroanimales'], null=False))
        ))
        db.create_unique('mapeo_asistenciatecnica_animales', ['asistenciatecnica_id', 'rubroanimales_id'])

        # Adding M2M table for field cultivos on 'AsistenciaTecnica'
        db.create_table('mapeo_asistenciatecnica_cultivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('asistenciatecnica', models.ForeignKey(orm['mapeo.asistenciatecnica'], null=False)),
            ('rubrocultivo', models.ForeignKey(orm['mapeo.rubrocultivo'], null=False))
        ))
        db.create_unique('mapeo_asistenciatecnica_cultivos', ['asistenciatecnica_id', 'rubrocultivo_id'])

        # Adding M2M table for field semillas on 'AsistenciaTecnica'
        db.create_table('mapeo_asistenciatecnica_semillas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('asistenciatecnica', models.ForeignKey(orm['mapeo.asistenciatecnica'], null=False)),
            ('semilla', models.ForeignKey(orm['mapeo.semilla'], null=False))
        ))
        db.create_unique('mapeo_asistenciatecnica_semillas', ['asistenciatecnica_id', 'semilla_id'])

        # Adding M2M table for field materia_procesada on 'AsistenciaTecnica'
        db.create_table('mapeo_asistenciatecnica_materia_procesada', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('asistenciatecnica', models.ForeignKey(orm['mapeo.asistenciatecnica'], null=False)),
            ('materiaprocesada', models.ForeignKey(orm['mapeo.materiaprocesada'], null=False))
        ))
        db.create_unique('mapeo_asistenciatecnica_materia_procesada', ['asistenciatecnica_id', 'materiaprocesada_id'])

        # Adding M2M table for field certificacion on 'AsistenciaTecnica'
        db.create_table('mapeo_asistenciatecnica_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('asistenciatecnica', models.ForeignKey(orm['mapeo.asistenciatecnica'], null=False)),
            ('certificacion', models.ForeignKey(orm['mapeo.certificacion'], null=False))
        ))
        db.create_unique('mapeo_asistenciatecnica_certificacion', ['asistenciatecnica_id', 'certificacion_id'])

        # Adding M2M table for field tipo_org on 'AsistenciaTecnica'
        db.create_table('mapeo_asistenciatecnica_tipo_org', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('asistenciatecnica', models.ForeignKey(orm['mapeo.asistenciatecnica'], null=False)),
            ('tipoorganizacion', models.ForeignKey(orm['mapeo.tipoorganizacion'], null=False))
        ))
        db.create_unique('mapeo_asistenciatecnica_tipo_org', ['asistenciatecnica_id', 'tipoorganizacion_id'])

        # Adding M2M table for field arboles on 'Familia'
        db.create_table('mapeo_familia_arboles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('familia', models.ForeignKey(orm['mapeo.familia'], null=False)),
            ('rubroarboles', models.ForeignKey(orm['mapeo.rubroarboles'], null=False))
        ))
        db.create_unique('mapeo_familia_arboles', ['familia_id', 'rubroarboles_id'])

        # Adding M2M table for field animales on 'Familia'
        db.create_table('mapeo_familia_animales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('familia', models.ForeignKey(orm['mapeo.familia'], null=False)),
            ('rubroanimales', models.ForeignKey(orm['mapeo.rubroanimales'], null=False))
        ))
        db.create_unique('mapeo_familia_animales', ['familia_id', 'rubroanimales_id'])

        # Adding M2M table for field cultivos on 'Familia'
        db.create_table('mapeo_familia_cultivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('familia', models.ForeignKey(orm['mapeo.familia'], null=False)),
            ('rubrocultivo', models.ForeignKey(orm['mapeo.rubrocultivo'], null=False))
        ))
        db.create_unique('mapeo_familia_cultivos', ['familia_id', 'rubrocultivo_id'])

        # Adding M2M table for field semillas on 'Familia'
        db.create_table('mapeo_familia_semillas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('familia', models.ForeignKey(orm['mapeo.familia'], null=False)),
            ('semilla', models.ForeignKey(orm['mapeo.semilla'], null=False))
        ))
        db.create_unique('mapeo_familia_semillas', ['familia_id', 'semilla_id'])

        # Adding M2M table for field materia_procesada on 'Familia'
        db.create_table('mapeo_familia_materia_procesada', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('familia', models.ForeignKey(orm['mapeo.familia'], null=False)),
            ('materiaprocesada', models.ForeignKey(orm['mapeo.materiaprocesada'], null=False))
        ))
        db.create_unique('mapeo_familia_materia_procesada', ['familia_id', 'materiaprocesada_id'])

        # Adding M2M table for field certificacion on 'Familia'
        db.create_table('mapeo_familia_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('familia', models.ForeignKey(orm['mapeo.familia'], null=False)),
            ('certificacion', models.ForeignKey(orm['mapeo.certificacion'], null=False))
        ))
        db.create_unique('mapeo_familia_certificacion', ['familia_id', 'certificacion_id'])

        # Adding M2M table for field tipo_org on 'Familia'
        db.create_table('mapeo_familia_tipo_org', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('familia', models.ForeignKey(orm['mapeo.familia'], null=False)),
            ('tipoorganizacion', models.ForeignKey(orm['mapeo.tipoorganizacion'], null=False))
        ))
        db.create_unique('mapeo_familia_tipo_org', ['familia_id', 'tipoorganizacion_id'])

        # Adding M2M table for field arboles on 'ComProducto'
        db.create_table('mapeo_comproducto_arboles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comproducto', models.ForeignKey(orm['mapeo.comproducto'], null=False)),
            ('rubroarboles', models.ForeignKey(orm['mapeo.rubroarboles'], null=False))
        ))
        db.create_unique('mapeo_comproducto_arboles', ['comproducto_id', 'rubroarboles_id'])

        # Adding M2M table for field animales on 'ComProducto'
        db.create_table('mapeo_comproducto_animales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comproducto', models.ForeignKey(orm['mapeo.comproducto'], null=False)),
            ('rubroanimales', models.ForeignKey(orm['mapeo.rubroanimales'], null=False))
        ))
        db.create_unique('mapeo_comproducto_animales', ['comproducto_id', 'rubroanimales_id'])

        # Adding M2M table for field cultivos on 'ComProducto'
        db.create_table('mapeo_comproducto_cultivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comproducto', models.ForeignKey(orm['mapeo.comproducto'], null=False)),
            ('rubrocultivo', models.ForeignKey(orm['mapeo.rubrocultivo'], null=False))
        ))
        db.create_unique('mapeo_comproducto_cultivos', ['comproducto_id', 'rubrocultivo_id'])

        # Adding M2M table for field semillas on 'ComProducto'
        db.create_table('mapeo_comproducto_semillas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comproducto', models.ForeignKey(orm['mapeo.comproducto'], null=False)),
            ('semilla', models.ForeignKey(orm['mapeo.semilla'], null=False))
        ))
        db.create_unique('mapeo_comproducto_semillas', ['comproducto_id', 'semilla_id'])

        # Adding M2M table for field materia_procesada on 'ComProducto'
        db.create_table('mapeo_comproducto_materia_procesada', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comproducto', models.ForeignKey(orm['mapeo.comproducto'], null=False)),
            ('materiaprocesada', models.ForeignKey(orm['mapeo.materiaprocesada'], null=False))
        ))
        db.create_unique('mapeo_comproducto_materia_procesada', ['comproducto_id', 'materiaprocesada_id'])

        # Adding M2M table for field certificacion on 'ComProducto'
        db.create_table('mapeo_comproducto_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comproducto', models.ForeignKey(orm['mapeo.comproducto'], null=False)),
            ('certificacion', models.ForeignKey(orm['mapeo.certificacion'], null=False))
        ))
        db.create_unique('mapeo_comproducto_certificacion', ['comproducto_id', 'certificacion_id'])

        # Adding M2M table for field tipo_prov on 'ComProducto'
        db.create_table('mapeo_comproducto_tipo_prov', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comproducto', models.ForeignKey(orm['mapeo.comproducto'], null=False)),
            ('tipoorganizacion', models.ForeignKey(orm['mapeo.tipoorganizacion'], null=False))
        ))
        db.create_unique('mapeo_comproducto_tipo_prov', ['comproducto_id', 'tipoorganizacion_id'])

        # Adding M2M table for field arboles on 'OrgPublica'
        db.create_table('mapeo_orgpublica_arboles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgpublica', models.ForeignKey(orm['mapeo.orgpublica'], null=False)),
            ('rubroarboles', models.ForeignKey(orm['mapeo.rubroarboles'], null=False))
        ))
        db.create_unique('mapeo_orgpublica_arboles', ['orgpublica_id', 'rubroarboles_id'])

        # Adding M2M table for field animales on 'OrgPublica'
        db.create_table('mapeo_orgpublica_animales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgpublica', models.ForeignKey(orm['mapeo.orgpublica'], null=False)),
            ('rubroanimales', models.ForeignKey(orm['mapeo.rubroanimales'], null=False))
        ))
        db.create_unique('mapeo_orgpublica_animales', ['orgpublica_id', 'rubroanimales_id'])

        # Adding M2M table for field cultivos on 'OrgPublica'
        db.create_table('mapeo_orgpublica_cultivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgpublica', models.ForeignKey(orm['mapeo.orgpublica'], null=False)),
            ('rubrocultivo', models.ForeignKey(orm['mapeo.rubrocultivo'], null=False))
        ))
        db.create_unique('mapeo_orgpublica_cultivos', ['orgpublica_id', 'rubrocultivo_id'])

        # Adding M2M table for field semillas on 'OrgPublica'
        db.create_table('mapeo_orgpublica_semillas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgpublica', models.ForeignKey(orm['mapeo.orgpublica'], null=False)),
            ('semilla', models.ForeignKey(orm['mapeo.semilla'], null=False))
        ))
        db.create_unique('mapeo_orgpublica_semillas', ['orgpublica_id', 'semilla_id'])

        # Adding M2M table for field materia_procesada on 'OrgPublica'
        db.create_table('mapeo_orgpublica_materia_procesada', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgpublica', models.ForeignKey(orm['mapeo.orgpublica'], null=False)),
            ('materiaprocesada', models.ForeignKey(orm['mapeo.materiaprocesada'], null=False))
        ))
        db.create_unique('mapeo_orgpublica_materia_procesada', ['orgpublica_id', 'materiaprocesada_id'])

        # Adding M2M table for field certificacion on 'OrgPublica'
        db.create_table('mapeo_orgpublica_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgpublica', models.ForeignKey(orm['mapeo.orgpublica'], null=False)),
            ('certificacion', models.ForeignKey(orm['mapeo.certificacion'], null=False))
        ))
        db.create_unique('mapeo_orgpublica_certificacion', ['orgpublica_id', 'certificacion_id'])

        # Adding M2M table for field area_trabajo on 'OrgPublica'
        db.create_table('mapeo_orgpublica_area_trabajo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgpublica', models.ForeignKey(orm['mapeo.orgpublica'], null=False)),
            ('areatrabajo', models.ForeignKey(orm['mapeo.areatrabajo'], null=False))
        ))
        db.create_unique('mapeo_orgpublica_area_trabajo', ['orgpublica_id', 'areatrabajo_id'])

        # Adding M2M table for field arboles on 'Certificadora'
        db.create_table('mapeo_certificadora_arboles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('certificadora', models.ForeignKey(orm['mapeo.certificadora'], null=False)),
            ('rubroarboles', models.ForeignKey(orm['mapeo.rubroarboles'], null=False))
        ))
        db.create_unique('mapeo_certificadora_arboles', ['certificadora_id', 'rubroarboles_id'])

        # Adding M2M table for field animales on 'Certificadora'
        db.create_table('mapeo_certificadora_animales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('certificadora', models.ForeignKey(orm['mapeo.certificadora'], null=False)),
            ('rubroanimales', models.ForeignKey(orm['mapeo.rubroanimales'], null=False))
        ))
        db.create_unique('mapeo_certificadora_animales', ['certificadora_id', 'rubroanimales_id'])

        # Adding M2M table for field cultivos on 'Certificadora'
        db.create_table('mapeo_certificadora_cultivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('certificadora', models.ForeignKey(orm['mapeo.certificadora'], null=False)),
            ('rubrocultivo', models.ForeignKey(orm['mapeo.rubrocultivo'], null=False))
        ))
        db.create_unique('mapeo_certificadora_cultivos', ['certificadora_id', 'rubrocultivo_id'])

        # Adding M2M table for field semillas on 'Certificadora'
        db.create_table('mapeo_certificadora_semillas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('certificadora', models.ForeignKey(orm['mapeo.certificadora'], null=False)),
            ('semilla', models.ForeignKey(orm['mapeo.semilla'], null=False))
        ))
        db.create_unique('mapeo_certificadora_semillas', ['certificadora_id', 'semilla_id'])

        # Adding M2M table for field materia_procesada on 'Certificadora'
        db.create_table('mapeo_certificadora_materia_procesada', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('certificadora', models.ForeignKey(orm['mapeo.certificadora'], null=False)),
            ('materiaprocesada', models.ForeignKey(orm['mapeo.materiaprocesada'], null=False))
        ))
        db.create_unique('mapeo_certificadora_materia_procesada', ['certificadora_id', 'materiaprocesada_id'])

        # Adding M2M table for field certificacion on 'Certificadora'
        db.create_table('mapeo_certificadora_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('certificadora', models.ForeignKey(orm['mapeo.certificadora'], null=False)),
            ('certificacion', models.ForeignKey(orm['mapeo.certificacion'], null=False))
        ))
        db.create_unique('mapeo_certificadora_certificacion', ['certificadora_id', 'certificacion_id'])

        # Adding M2M table for field tipo_cliente on 'Certificadora'
        db.create_table('mapeo_certificadora_tipo_cliente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('certificadora', models.ForeignKey(orm['mapeo.certificadora'], null=False)),
            ('tipoorganizacion', models.ForeignKey(orm['mapeo.tipoorganizacion'], null=False))
        ))
        db.create_unique('mapeo_certificadora_tipo_cliente', ['certificadora_id', 'tipoorganizacion_id'])

        # Adding M2M table for field arboles on 'Cooperativa'
        db.create_table('mapeo_cooperativa_arboles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cooperativa', models.ForeignKey(orm['mapeo.cooperativa'], null=False)),
            ('rubroarboles', models.ForeignKey(orm['mapeo.rubroarboles'], null=False))
        ))
        db.create_unique('mapeo_cooperativa_arboles', ['cooperativa_id', 'rubroarboles_id'])

        # Adding M2M table for field animales on 'Cooperativa'
        db.create_table('mapeo_cooperativa_animales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cooperativa', models.ForeignKey(orm['mapeo.cooperativa'], null=False)),
            ('rubroanimales', models.ForeignKey(orm['mapeo.rubroanimales'], null=False))
        ))
        db.create_unique('mapeo_cooperativa_animales', ['cooperativa_id', 'rubroanimales_id'])

        # Adding M2M table for field cultivos on 'Cooperativa'
        db.create_table('mapeo_cooperativa_cultivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cooperativa', models.ForeignKey(orm['mapeo.cooperativa'], null=False)),
            ('rubrocultivo', models.ForeignKey(orm['mapeo.rubrocultivo'], null=False))
        ))
        db.create_unique('mapeo_cooperativa_cultivos', ['cooperativa_id', 'rubrocultivo_id'])

        # Adding M2M table for field semillas on 'Cooperativa'
        db.create_table('mapeo_cooperativa_semillas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cooperativa', models.ForeignKey(orm['mapeo.cooperativa'], null=False)),
            ('semilla', models.ForeignKey(orm['mapeo.semilla'], null=False))
        ))
        db.create_unique('mapeo_cooperativa_semillas', ['cooperativa_id', 'semilla_id'])

        # Adding M2M table for field materia_procesada on 'Cooperativa'
        db.create_table('mapeo_cooperativa_materia_procesada', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cooperativa', models.ForeignKey(orm['mapeo.cooperativa'], null=False)),
            ('materiaprocesada', models.ForeignKey(orm['mapeo.materiaprocesada'], null=False))
        ))
        db.create_unique('mapeo_cooperativa_materia_procesada', ['cooperativa_id', 'materiaprocesada_id'])

        # Adding M2M table for field certificacion on 'Cooperativa'
        db.create_table('mapeo_cooperativa_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cooperativa', models.ForeignKey(orm['mapeo.cooperativa'], null=False)),
            ('certificacion', models.ForeignKey(orm['mapeo.certificacion'], null=False))
        ))
        db.create_unique('mapeo_cooperativa_certificacion', ['cooperativa_id', 'certificacion_id'])

        # Adding M2M table for field area_trabajo on 'Cooperativa'
        db.create_table('mapeo_cooperativa_area_trabajo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cooperativa', models.ForeignKey(orm['mapeo.cooperativa'], null=False)),
            ('areatrabajo', models.ForeignKey(orm['mapeo.areatrabajo'], null=False))
        ))
        db.create_unique('mapeo_cooperativa_area_trabajo', ['cooperativa_id', 'areatrabajo_id'])

        # Adding M2M table for field arboles on 'ComInsumo'
        db.create_table('mapeo_cominsumo_arboles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cominsumo', models.ForeignKey(orm['mapeo.cominsumo'], null=False)),
            ('rubroarboles', models.ForeignKey(orm['mapeo.rubroarboles'], null=False))
        ))
        db.create_unique('mapeo_cominsumo_arboles', ['cominsumo_id', 'rubroarboles_id'])

        # Adding M2M table for field animales on 'ComInsumo'
        db.create_table('mapeo_cominsumo_animales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cominsumo', models.ForeignKey(orm['mapeo.cominsumo'], null=False)),
            ('rubroanimales', models.ForeignKey(orm['mapeo.rubroanimales'], null=False))
        ))
        db.create_unique('mapeo_cominsumo_animales', ['cominsumo_id', 'rubroanimales_id'])

        # Adding M2M table for field cultivos on 'ComInsumo'
        db.create_table('mapeo_cominsumo_cultivos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cominsumo', models.ForeignKey(orm['mapeo.cominsumo'], null=False)),
            ('rubrocultivo', models.ForeignKey(orm['mapeo.rubrocultivo'], null=False))
        ))
        db.create_unique('mapeo_cominsumo_cultivos', ['cominsumo_id', 'rubrocultivo_id'])

        # Adding M2M table for field semillas on 'ComInsumo'
        db.create_table('mapeo_cominsumo_semillas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cominsumo', models.ForeignKey(orm['mapeo.cominsumo'], null=False)),
            ('semilla', models.ForeignKey(orm['mapeo.semilla'], null=False))
        ))
        db.create_unique('mapeo_cominsumo_semillas', ['cominsumo_id', 'semilla_id'])

        # Adding M2M table for field materia_procesada on 'ComInsumo'
        db.create_table('mapeo_cominsumo_materia_procesada', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cominsumo', models.ForeignKey(orm['mapeo.cominsumo'], null=False)),
            ('materiaprocesada', models.ForeignKey(orm['mapeo.materiaprocesada'], null=False))
        ))
        db.create_unique('mapeo_cominsumo_materia_procesada', ['cominsumo_id', 'materiaprocesada_id'])

        # Adding M2M table for field certificacion on 'ComInsumo'
        db.create_table('mapeo_cominsumo_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cominsumo', models.ForeignKey(orm['mapeo.cominsumo'], null=False)),
            ('certificacion', models.ForeignKey(orm['mapeo.certificacion'], null=False))
        ))
        db.create_unique('mapeo_cominsumo_certificacion', ['cominsumo_id', 'certificacion_id'])

        # Adding M2M table for field tipo_cliente on 'ComInsumo'
        db.create_table('mapeo_cominsumo_tipo_cliente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cominsumo', models.ForeignKey(orm['mapeo.cominsumo'], null=False)),
            ('tipoorganizacion', models.ForeignKey(orm['mapeo.tipoorganizacion'], null=False))
        ))
        db.create_unique('mapeo_cominsumo_tipo_cliente', ['cominsumo_id', 'tipoorganizacion_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field arboles on 'Financiera'
        db.delete_table('mapeo_financiera_arboles')

        # Removing M2M table for field animales on 'Financiera'
        db.delete_table('mapeo_financiera_animales')

        # Removing M2M table for field cultivos on 'Financiera'
        db.delete_table('mapeo_financiera_cultivos')

        # Removing M2M table for field semillas on 'Financiera'
        db.delete_table('mapeo_financiera_semillas')

        # Removing M2M table for field materia_procesada on 'Financiera'
        db.delete_table('mapeo_financiera_materia_procesada')

        # Removing M2M table for field certificacion on 'Financiera'
        db.delete_table('mapeo_financiera_certificacion')

        # Removing M2M table for field tipo_cliente on 'Financiera'
        db.delete_table('mapeo_financiera_tipo_cliente')

        # Removing M2M table for field arboles on 'OrgAcompanante'
        db.delete_table('mapeo_orgacompanante_arboles')

        # Removing M2M table for field animales on 'OrgAcompanante'
        db.delete_table('mapeo_orgacompanante_animales')

        # Removing M2M table for field cultivos on 'OrgAcompanante'
        db.delete_table('mapeo_orgacompanante_cultivos')

        # Removing M2M table for field semillas on 'OrgAcompanante'
        db.delete_table('mapeo_orgacompanante_semillas')

        # Removing M2M table for field materia_procesada on 'OrgAcompanante'
        db.delete_table('mapeo_orgacompanante_materia_procesada')

        # Removing M2M table for field certificacion on 'OrgAcompanante'
        db.delete_table('mapeo_orgacompanante_certificacion')

        # Removing M2M table for field arboles on 'Centrales'
        db.delete_table('mapeo_centrales_arboles')

        # Removing M2M table for field animales on 'Centrales'
        db.delete_table('mapeo_centrales_animales')

        # Removing M2M table for field cultivos on 'Centrales'
        db.delete_table('mapeo_centrales_cultivos')

        # Removing M2M table for field semillas on 'Centrales'
        db.delete_table('mapeo_centrales_semillas')

        # Removing M2M table for field materia_procesada on 'Centrales'
        db.delete_table('mapeo_centrales_materia_procesada')

        # Removing M2M table for field certificacion on 'Centrales'
        db.delete_table('mapeo_centrales_certificacion')

        # Removing M2M table for field area_trabajo on 'Centrales'
        db.delete_table('mapeo_centrales_area_trabajo')

        # Removing M2M table for field arboles on 'AsistenciaTecnica'
        db.delete_table('mapeo_asistenciatecnica_arboles')

        # Removing M2M table for field animales on 'AsistenciaTecnica'
        db.delete_table('mapeo_asistenciatecnica_animales')

        # Removing M2M table for field cultivos on 'AsistenciaTecnica'
        db.delete_table('mapeo_asistenciatecnica_cultivos')

        # Removing M2M table for field semillas on 'AsistenciaTecnica'
        db.delete_table('mapeo_asistenciatecnica_semillas')

        # Removing M2M table for field materia_procesada on 'AsistenciaTecnica'
        db.delete_table('mapeo_asistenciatecnica_materia_procesada')

        # Removing M2M table for field certificacion on 'AsistenciaTecnica'
        db.delete_table('mapeo_asistenciatecnica_certificacion')

        # Removing M2M table for field tipo_org on 'AsistenciaTecnica'
        db.delete_table('mapeo_asistenciatecnica_tipo_org')

        # Removing M2M table for field arboles on 'Familia'
        db.delete_table('mapeo_familia_arboles')

        # Removing M2M table for field animales on 'Familia'
        db.delete_table('mapeo_familia_animales')

        # Removing M2M table for field cultivos on 'Familia'
        db.delete_table('mapeo_familia_cultivos')

        # Removing M2M table for field semillas on 'Familia'
        db.delete_table('mapeo_familia_semillas')

        # Removing M2M table for field materia_procesada on 'Familia'
        db.delete_table('mapeo_familia_materia_procesada')

        # Removing M2M table for field certificacion on 'Familia'
        db.delete_table('mapeo_familia_certificacion')

        # Removing M2M table for field tipo_org on 'Familia'
        db.delete_table('mapeo_familia_tipo_org')

        # Removing M2M table for field arboles on 'ComProducto'
        db.delete_table('mapeo_comproducto_arboles')

        # Removing M2M table for field animales on 'ComProducto'
        db.delete_table('mapeo_comproducto_animales')

        # Removing M2M table for field cultivos on 'ComProducto'
        db.delete_table('mapeo_comproducto_cultivos')

        # Removing M2M table for field semillas on 'ComProducto'
        db.delete_table('mapeo_comproducto_semillas')

        # Removing M2M table for field materia_procesada on 'ComProducto'
        db.delete_table('mapeo_comproducto_materia_procesada')

        # Removing M2M table for field certificacion on 'ComProducto'
        db.delete_table('mapeo_comproducto_certificacion')

        # Removing M2M table for field tipo_prov on 'ComProducto'
        db.delete_table('mapeo_comproducto_tipo_prov')

        # Removing M2M table for field arboles on 'OrgPublica'
        db.delete_table('mapeo_orgpublica_arboles')

        # Removing M2M table for field animales on 'OrgPublica'
        db.delete_table('mapeo_orgpublica_animales')

        # Removing M2M table for field cultivos on 'OrgPublica'
        db.delete_table('mapeo_orgpublica_cultivos')

        # Removing M2M table for field semillas on 'OrgPublica'
        db.delete_table('mapeo_orgpublica_semillas')

        # Removing M2M table for field materia_procesada on 'OrgPublica'
        db.delete_table('mapeo_orgpublica_materia_procesada')

        # Removing M2M table for field certificacion on 'OrgPublica'
        db.delete_table('mapeo_orgpublica_certificacion')

        # Removing M2M table for field area_trabajo on 'OrgPublica'
        db.delete_table('mapeo_orgpublica_area_trabajo')

        # Removing M2M table for field arboles on 'Certificadora'
        db.delete_table('mapeo_certificadora_arboles')

        # Removing M2M table for field animales on 'Certificadora'
        db.delete_table('mapeo_certificadora_animales')

        # Removing M2M table for field cultivos on 'Certificadora'
        db.delete_table('mapeo_certificadora_cultivos')

        # Removing M2M table for field semillas on 'Certificadora'
        db.delete_table('mapeo_certificadora_semillas')

        # Removing M2M table for field materia_procesada on 'Certificadora'
        db.delete_table('mapeo_certificadora_materia_procesada')

        # Removing M2M table for field certificacion on 'Certificadora'
        db.delete_table('mapeo_certificadora_certificacion')

        # Removing M2M table for field tipo_cliente on 'Certificadora'
        db.delete_table('mapeo_certificadora_tipo_cliente')

        # Removing M2M table for field arboles on 'Cooperativa'
        db.delete_table('mapeo_cooperativa_arboles')

        # Removing M2M table for field animales on 'Cooperativa'
        db.delete_table('mapeo_cooperativa_animales')

        # Removing M2M table for field cultivos on 'Cooperativa'
        db.delete_table('mapeo_cooperativa_cultivos')

        # Removing M2M table for field semillas on 'Cooperativa'
        db.delete_table('mapeo_cooperativa_semillas')

        # Removing M2M table for field materia_procesada on 'Cooperativa'
        db.delete_table('mapeo_cooperativa_materia_procesada')

        # Removing M2M table for field certificacion on 'Cooperativa'
        db.delete_table('mapeo_cooperativa_certificacion')

        # Removing M2M table for field area_trabajo on 'Cooperativa'
        db.delete_table('mapeo_cooperativa_area_trabajo')

        # Removing M2M table for field arboles on 'ComInsumo'
        db.delete_table('mapeo_cominsumo_arboles')

        # Removing M2M table for field animales on 'ComInsumo'
        db.delete_table('mapeo_cominsumo_animales')

        # Removing M2M table for field cultivos on 'ComInsumo'
        db.delete_table('mapeo_cominsumo_cultivos')

        # Removing M2M table for field semillas on 'ComInsumo'
        db.delete_table('mapeo_cominsumo_semillas')

        # Removing M2M table for field materia_procesada on 'ComInsumo'
        db.delete_table('mapeo_cominsumo_materia_procesada')

        # Removing M2M table for field certificacion on 'ComInsumo'
        db.delete_table('mapeo_cominsumo_certificacion')

        # Removing M2M table for field tipo_cliente on 'ComInsumo'
        db.delete_table('mapeo_cominsumo_tipo_cliente')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'mapeo.areatrabajo': {
            'Meta': {'object_name': 'AreaTrabajo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.asistenciatecnica': {
            'Meta': {'object_name': 'AsistenciaTecnica'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_org': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.buenaspracticas': {
            'Meta': {'object_name': 'BuenasPracticas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.centrales': {
            'Meta': {'object_name': 'Centrales'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_est': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'num_asociaciones': ('django.db.models.fields.IntegerField', [], {}),
            'num_cooperativas': ('django.db.models.fields.IntegerField', [], {}),
            'num_hombres': ('django.db.models.fields.IntegerField', [], {}),
            'num_mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.certificacion': {
            'Meta': {'object_name': 'Certificacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.certificadora': {
            'Meta': {'object_name': 'Certificadora'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.cominsumo': {
            'Meta': {'object_name': 'ComInsumo'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False'}),
            'desde_insumo': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.comproducto': {
            'Meta': {'object_name': 'ComProducto'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_prov': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.cooperativa': {
            'Meta': {'object_name': 'Cooperativa'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_est': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'num_hombres': ('django.db.models.fields.IntegerField', [], {}),
            'num_mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.familia': {
            'Meta': {'object_name': 'Familia'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'area_finca': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre_finca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_org': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.financiera': {
            'Meta': {'object_name': 'Financiera'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.materiaprocesada': {
            'Meta': {'object_name': 'MateriaProcesada'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.orgacompanante': {
            'Meta': {'object_name': 'OrgAcompanante'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.orgpublica': {
            'Meta': {'object_name': 'OrgPublica'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.rubroanimales': {
            'Meta': {'object_name': 'RubroAnimales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.rubroarboles': {
            'Meta': {'object_name': 'RubroArboles'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.rubrocultivo': {
            'Meta': {'object_name': 'RubroCultivo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.semilla': {
            'Meta': {'object_name': 'Semilla'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.tipoorganizacion': {
            'Meta': {'object_name': 'TipoOrganizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['mapeo']
