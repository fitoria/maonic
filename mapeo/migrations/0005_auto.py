# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field buenas_practicas on 'Financiera'
        db.create_table('mapeo_financiera_buenas_practicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('financiera', models.ForeignKey(orm['mapeo.financiera'], null=False)),
            ('buenaspracticas', models.ForeignKey(orm['mapeo.buenaspracticas'], null=False))
        ))
        db.create_unique('mapeo_financiera_buenas_practicas', ['financiera_id', 'buenaspracticas_id'])

        # Adding M2M table for field buenas_practicas on 'Centrales'
        db.create_table('mapeo_centrales_buenas_practicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centrales', models.ForeignKey(orm['mapeo.centrales'], null=False)),
            ('buenaspracticas', models.ForeignKey(orm['mapeo.buenaspracticas'], null=False))
        ))
        db.create_unique('mapeo_centrales_buenas_practicas', ['centrales_id', 'buenaspracticas_id'])

        # Adding M2M table for field buenas_practicas on 'AsistenciaTecnica'
        db.create_table('mapeo_asistenciatecnica_buenas_practicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('asistenciatecnica', models.ForeignKey(orm['mapeo.asistenciatecnica'], null=False)),
            ('buenaspracticas', models.ForeignKey(orm['mapeo.buenaspracticas'], null=False))
        ))
        db.create_unique('mapeo_asistenciatecnica_buenas_practicas', ['asistenciatecnica_id', 'buenaspracticas_id'])

        # Adding M2M table for field buenas_practicas on 'Familia'
        db.create_table('mapeo_familia_buenas_practicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('familia', models.ForeignKey(orm['mapeo.familia'], null=False)),
            ('buenaspracticas', models.ForeignKey(orm['mapeo.buenaspracticas'], null=False))
        ))
        db.create_unique('mapeo_familia_buenas_practicas', ['familia_id', 'buenaspracticas_id'])

        # Adding M2M table for field buenas_practicas on 'ComProducto'
        db.create_table('mapeo_comproducto_buenas_practicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comproducto', models.ForeignKey(orm['mapeo.comproducto'], null=False)),
            ('buenaspracticas', models.ForeignKey(orm['mapeo.buenaspracticas'], null=False))
        ))
        db.create_unique('mapeo_comproducto_buenas_practicas', ['comproducto_id', 'buenaspracticas_id'])

        # Adding M2M table for field buenas_practicas on 'OrgPublica'
        db.create_table('mapeo_orgpublica_buenas_practicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orgpublica', models.ForeignKey(orm['mapeo.orgpublica'], null=False)),
            ('buenaspracticas', models.ForeignKey(orm['mapeo.buenaspracticas'], null=False))
        ))
        db.create_unique('mapeo_orgpublica_buenas_practicas', ['orgpublica_id', 'buenaspracticas_id'])

        # Adding M2M table for field buenas_practicas on 'Certificadora'
        db.create_table('mapeo_certificadora_buenas_practicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('certificadora', models.ForeignKey(orm['mapeo.certificadora'], null=False)),
            ('buenaspracticas', models.ForeignKey(orm['mapeo.buenaspracticas'], null=False))
        ))
        db.create_unique('mapeo_certificadora_buenas_practicas', ['certificadora_id', 'buenaspracticas_id'])

        # Adding M2M table for field buenas_practicas on 'Cooperativa'
        db.create_table('mapeo_cooperativa_buenas_practicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cooperativa', models.ForeignKey(orm['mapeo.cooperativa'], null=False)),
            ('buenaspracticas', models.ForeignKey(orm['mapeo.buenaspracticas'], null=False))
        ))
        db.create_unique('mapeo_cooperativa_buenas_practicas', ['cooperativa_id', 'buenaspracticas_id'])

        # Adding M2M table for field buenas_practicas on 'ComInsumo'
        db.create_table('mapeo_cominsumo_buenas_practicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cominsumo', models.ForeignKey(orm['mapeo.cominsumo'], null=False)),
            ('buenaspracticas', models.ForeignKey(orm['mapeo.buenaspracticas'], null=False))
        ))
        db.create_unique('mapeo_cominsumo_buenas_practicas', ['cominsumo_id', 'buenaspracticas_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field buenas_practicas on 'Financiera'
        db.delete_table('mapeo_financiera_buenas_practicas')

        # Removing M2M table for field buenas_practicas on 'Centrales'
        db.delete_table('mapeo_centrales_buenas_practicas')

        # Removing M2M table for field buenas_practicas on 'AsistenciaTecnica'
        db.delete_table('mapeo_asistenciatecnica_buenas_practicas')

        # Removing M2M table for field buenas_practicas on 'Familia'
        db.delete_table('mapeo_familia_buenas_practicas')

        # Removing M2M table for field buenas_practicas on 'ComProducto'
        db.delete_table('mapeo_comproducto_buenas_practicas')

        # Removing M2M table for field buenas_practicas on 'OrgPublica'
        db.delete_table('mapeo_orgpublica_buenas_practicas')

        # Removing M2M table for field buenas_practicas on 'Certificadora'
        db.delete_table('mapeo_certificadora_buenas_practicas')

        # Removing M2M table for field buenas_practicas on 'Cooperativa'
        db.delete_table('mapeo_cooperativa_buenas_practicas')

        # Removing M2M table for field buenas_practicas on 'ComInsumo'
        db.delete_table('mapeo_cominsumo_buenas_practicas')


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
            'tipo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoUsuario']", 'symmetrical': 'False'}),
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
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False'}),
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
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False'}),
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
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False'}),
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
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False'}),
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
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False'}),
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
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False'}),
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
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False'}),
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
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False'}),
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
        'mapeo.orgpublica': {
            'Meta': {'object_name': 'OrgPublica'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False'}),
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False'}),
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
        },
        'mapeo.tipousuario': {
            'Meta': {'object_name': 'TipoUsuario'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['mapeo']
