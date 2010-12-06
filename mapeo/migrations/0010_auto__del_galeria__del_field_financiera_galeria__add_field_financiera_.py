# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Galeria'
        db.delete_table('mapeo_galeria')

        # Deleting field 'Financiera.galeria'
        db.delete_column('mapeo_financiera', 'galeria_id')

        # Adding field 'Financiera.foto1'
        db.add_column('mapeo_financiera', 'foto1', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Financiera.foto2'
        db.add_column('mapeo_financiera', 'foto2', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Financiera.foto3'
        db.add_column('mapeo_financiera', 'foto3', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Financiera.foto4'
        db.add_column('mapeo_financiera', 'foto4', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Financiera.foto5'
        db.add_column('mapeo_financiera', 'foto5', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'Centrales.galeria'
        db.delete_column('mapeo_centrales', 'galeria_id')

        # Adding field 'Centrales.foto1'
        db.add_column('mapeo_centrales', 'foto1', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Centrales.foto2'
        db.add_column('mapeo_centrales', 'foto2', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Centrales.foto3'
        db.add_column('mapeo_centrales', 'foto3', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Centrales.foto4'
        db.add_column('mapeo_centrales', 'foto4', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Centrales.foto5'
        db.add_column('mapeo_centrales', 'foto5', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'AsistenciaTecnica.galeria'
        db.delete_column('mapeo_asistenciatecnica', 'galeria_id')

        # Adding field 'AsistenciaTecnica.foto1'
        db.add_column('mapeo_asistenciatecnica', 'foto1', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'AsistenciaTecnica.foto2'
        db.add_column('mapeo_asistenciatecnica', 'foto2', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'AsistenciaTecnica.foto3'
        db.add_column('mapeo_asistenciatecnica', 'foto3', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'AsistenciaTecnica.foto4'
        db.add_column('mapeo_asistenciatecnica', 'foto4', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'AsistenciaTecnica.foto5'
        db.add_column('mapeo_asistenciatecnica', 'foto5', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'Familia.galeria'
        db.delete_column('mapeo_familia', 'galeria_id')

        # Adding field 'Familia.foto1'
        db.add_column('mapeo_familia', 'foto1', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Familia.foto2'
        db.add_column('mapeo_familia', 'foto2', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Familia.foto3'
        db.add_column('mapeo_familia', 'foto3', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Familia.foto4'
        db.add_column('mapeo_familia', 'foto4', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Familia.foto5'
        db.add_column('mapeo_familia', 'foto5', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'ComProducto.galeria'
        db.delete_column('mapeo_comproducto', 'galeria_id')

        # Adding field 'ComProducto.foto1'
        db.add_column('mapeo_comproducto', 'foto1', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'ComProducto.foto2'
        db.add_column('mapeo_comproducto', 'foto2', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'ComProducto.foto3'
        db.add_column('mapeo_comproducto', 'foto3', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'ComProducto.foto4'
        db.add_column('mapeo_comproducto', 'foto4', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'ComProducto.foto5'
        db.add_column('mapeo_comproducto', 'foto5', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'OrgPublica.galeria'
        db.delete_column('mapeo_orgpublica', 'galeria_id')

        # Adding field 'OrgPublica.foto1'
        db.add_column('mapeo_orgpublica', 'foto1', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'OrgPublica.foto2'
        db.add_column('mapeo_orgpublica', 'foto2', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'OrgPublica.foto3'
        db.add_column('mapeo_orgpublica', 'foto3', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'OrgPublica.foto4'
        db.add_column('mapeo_orgpublica', 'foto4', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'OrgPublica.foto5'
        db.add_column('mapeo_orgpublica', 'foto5', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'Certificadora.galeria'
        db.delete_column('mapeo_certificadora', 'galeria_id')

        # Adding field 'Certificadora.foto1'
        db.add_column('mapeo_certificadora', 'foto1', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Certificadora.foto2'
        db.add_column('mapeo_certificadora', 'foto2', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Certificadora.foto3'
        db.add_column('mapeo_certificadora', 'foto3', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Certificadora.foto4'
        db.add_column('mapeo_certificadora', 'foto4', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Certificadora.foto5'
        db.add_column('mapeo_certificadora', 'foto5', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'Cooperativa.galeria'
        db.delete_column('mapeo_cooperativa', 'galeria_id')

        # Adding field 'Cooperativa.foto1'
        db.add_column('mapeo_cooperativa', 'foto1', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Cooperativa.foto2'
        db.add_column('mapeo_cooperativa', 'foto2', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Cooperativa.foto3'
        db.add_column('mapeo_cooperativa', 'foto3', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Cooperativa.foto4'
        db.add_column('mapeo_cooperativa', 'foto4', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Cooperativa.foto5'
        db.add_column('mapeo_cooperativa', 'foto5', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'ComInsumo.galeria'
        db.delete_column('mapeo_cominsumo', 'galeria_id')

        # Adding field 'ComInsumo.foto1'
        db.add_column('mapeo_cominsumo', 'foto1', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'ComInsumo.foto2'
        db.add_column('mapeo_cominsumo', 'foto2', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'ComInsumo.foto3'
        db.add_column('mapeo_cominsumo', 'foto3', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'ComInsumo.foto4'
        db.add_column('mapeo_cominsumo', 'foto4', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'ComInsumo.foto5'
        db.add_column('mapeo_cominsumo', 'foto5', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Galeria'
        db.create_table('mapeo_galeria', (
            ('foto5', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('foto3', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('foto2', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('foto1', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto4', self.gf('maonic.mapeo.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('mapeo', ['Galeria'])

        # Adding field 'Financiera.galeria'
        db.add_column('mapeo_financiera', 'galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Galeria'], null=True), keep_default=False)

        # Deleting field 'Financiera.foto1'
        db.delete_column('mapeo_financiera', 'foto1')

        # Deleting field 'Financiera.foto2'
        db.delete_column('mapeo_financiera', 'foto2')

        # Deleting field 'Financiera.foto3'
        db.delete_column('mapeo_financiera', 'foto3')

        # Deleting field 'Financiera.foto4'
        db.delete_column('mapeo_financiera', 'foto4')

        # Deleting field 'Financiera.foto5'
        db.delete_column('mapeo_financiera', 'foto5')

        # Adding field 'Centrales.galeria'
        db.add_column('mapeo_centrales', 'galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Galeria'], null=True), keep_default=False)

        # Deleting field 'Centrales.foto1'
        db.delete_column('mapeo_centrales', 'foto1')

        # Deleting field 'Centrales.foto2'
        db.delete_column('mapeo_centrales', 'foto2')

        # Deleting field 'Centrales.foto3'
        db.delete_column('mapeo_centrales', 'foto3')

        # Deleting field 'Centrales.foto4'
        db.delete_column('mapeo_centrales', 'foto4')

        # Deleting field 'Centrales.foto5'
        db.delete_column('mapeo_centrales', 'foto5')

        # Adding field 'AsistenciaTecnica.galeria'
        db.add_column('mapeo_asistenciatecnica', 'galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Galeria'], null=True), keep_default=False)

        # Deleting field 'AsistenciaTecnica.foto1'
        db.delete_column('mapeo_asistenciatecnica', 'foto1')

        # Deleting field 'AsistenciaTecnica.foto2'
        db.delete_column('mapeo_asistenciatecnica', 'foto2')

        # Deleting field 'AsistenciaTecnica.foto3'
        db.delete_column('mapeo_asistenciatecnica', 'foto3')

        # Deleting field 'AsistenciaTecnica.foto4'
        db.delete_column('mapeo_asistenciatecnica', 'foto4')

        # Deleting field 'AsistenciaTecnica.foto5'
        db.delete_column('mapeo_asistenciatecnica', 'foto5')

        # Adding field 'Familia.galeria'
        db.add_column('mapeo_familia', 'galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Galeria'], null=True), keep_default=False)

        # Deleting field 'Familia.foto1'
        db.delete_column('mapeo_familia', 'foto1')

        # Deleting field 'Familia.foto2'
        db.delete_column('mapeo_familia', 'foto2')

        # Deleting field 'Familia.foto3'
        db.delete_column('mapeo_familia', 'foto3')

        # Deleting field 'Familia.foto4'
        db.delete_column('mapeo_familia', 'foto4')

        # Deleting field 'Familia.foto5'
        db.delete_column('mapeo_familia', 'foto5')

        # Adding field 'ComProducto.galeria'
        db.add_column('mapeo_comproducto', 'galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Galeria'], null=True), keep_default=False)

        # Deleting field 'ComProducto.foto1'
        db.delete_column('mapeo_comproducto', 'foto1')

        # Deleting field 'ComProducto.foto2'
        db.delete_column('mapeo_comproducto', 'foto2')

        # Deleting field 'ComProducto.foto3'
        db.delete_column('mapeo_comproducto', 'foto3')

        # Deleting field 'ComProducto.foto4'
        db.delete_column('mapeo_comproducto', 'foto4')

        # Deleting field 'ComProducto.foto5'
        db.delete_column('mapeo_comproducto', 'foto5')

        # Adding field 'OrgPublica.galeria'
        db.add_column('mapeo_orgpublica', 'galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Galeria'], null=True), keep_default=False)

        # Deleting field 'OrgPublica.foto1'
        db.delete_column('mapeo_orgpublica', 'foto1')

        # Deleting field 'OrgPublica.foto2'
        db.delete_column('mapeo_orgpublica', 'foto2')

        # Deleting field 'OrgPublica.foto3'
        db.delete_column('mapeo_orgpublica', 'foto3')

        # Deleting field 'OrgPublica.foto4'
        db.delete_column('mapeo_orgpublica', 'foto4')

        # Deleting field 'OrgPublica.foto5'
        db.delete_column('mapeo_orgpublica', 'foto5')

        # Adding field 'Certificadora.galeria'
        db.add_column('mapeo_certificadora', 'galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Galeria'], null=True), keep_default=False)

        # Deleting field 'Certificadora.foto1'
        db.delete_column('mapeo_certificadora', 'foto1')

        # Deleting field 'Certificadora.foto2'
        db.delete_column('mapeo_certificadora', 'foto2')

        # Deleting field 'Certificadora.foto3'
        db.delete_column('mapeo_certificadora', 'foto3')

        # Deleting field 'Certificadora.foto4'
        db.delete_column('mapeo_certificadora', 'foto4')

        # Deleting field 'Certificadora.foto5'
        db.delete_column('mapeo_certificadora', 'foto5')

        # Adding field 'Cooperativa.galeria'
        db.add_column('mapeo_cooperativa', 'galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Galeria'], null=True), keep_default=False)

        # Deleting field 'Cooperativa.foto1'
        db.delete_column('mapeo_cooperativa', 'foto1')

        # Deleting field 'Cooperativa.foto2'
        db.delete_column('mapeo_cooperativa', 'foto2')

        # Deleting field 'Cooperativa.foto3'
        db.delete_column('mapeo_cooperativa', 'foto3')

        # Deleting field 'Cooperativa.foto4'
        db.delete_column('mapeo_cooperativa', 'foto4')

        # Deleting field 'Cooperativa.foto5'
        db.delete_column('mapeo_cooperativa', 'foto5')

        # Adding field 'ComInsumo.galeria'
        db.add_column('mapeo_cominsumo', 'galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Galeria'], null=True), keep_default=False)

        # Deleting field 'ComInsumo.foto1'
        db.delete_column('mapeo_cominsumo', 'foto1')

        # Deleting field 'ComInsumo.foto2'
        db.delete_column('mapeo_cominsumo', 'foto2')

        # Deleting field 'ComInsumo.foto3'
        db.delete_column('mapeo_cominsumo', 'foto3')

        # Deleting field 'ComInsumo.foto4'
        db.delete_column('mapeo_cominsumo', 'foto4')

        # Deleting field 'ComInsumo.foto5'
        db.delete_column('mapeo_cominsumo', 'foto5')


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
            'Meta': {'ordering': "['nombre']", 'object_name': 'AreaTrabajo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.asistenciatecnica': {
            'Meta': {'object_name': 'AsistenciaTecnica'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_org': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.buenaspracticas': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'BuenasPracticas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.centrales': {
            'Meta': {'object_name': 'Centrales'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_est': ('django.db.models.fields.DateField', [], {}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'num_asociaciones': ('django.db.models.fields.IntegerField', [], {}),
            'num_cooperativas': ('django.db.models.fields.IntegerField', [], {}),
            'num_hombres': ('django.db.models.fields.IntegerField', [], {}),
            'num_mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.certificacion': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Certificacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.certificadora': {
            'Meta': {'object_name': 'Certificadora'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.cominsumo': {
            'Meta': {'object_name': 'ComInsumo'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'desde_insumo': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.comproducto': {
            'Meta': {'object_name': 'ComProducto'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_prov': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.cooperativa': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Cooperativa'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_est': ('django.db.models.fields.DateField', [], {}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'num_hombres': ('django.db.models.fields.IntegerField', [], {}),
            'num_mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.familia': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Familia'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'area_finca': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre_finca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_org': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.financiera': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Financiera'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.IntegerField', [], {}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.TipoOrganizacion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.materiaprocesada': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'MateriaProcesada'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.orgpublica': {
            'Meta': {'object_name': 'OrgPublica'},
            'animales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroAnimales']", 'symmetrical': 'False', 'blank': 'True'}),
            'arboles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroArboles']", 'symmetrical': 'False', 'blank': 'True'}),
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.AreaTrabajo']", 'symmetrical': 'False'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.BuenasPracticas']", 'symmetrical': 'False', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Certificacion']", 'symmetrical': 'False', 'blank': 'True'}),
            'cultivos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.RubroCultivo']", 'symmetrical': 'False', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_agregado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto1': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto5': ('maonic.mapeo.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'materia_procesada': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.MateriaProcesada']", 'symmetrical': 'False', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semillas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mapeo.Semilla']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mapeo.rubroanimales': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'RubroAnimales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.rubroarboles': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'RubroArboles'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.rubrocultivo': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'RubroCultivo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.semilla': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Semilla'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mapeo.tipoorganizacion': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'TipoOrganizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['mapeo']
