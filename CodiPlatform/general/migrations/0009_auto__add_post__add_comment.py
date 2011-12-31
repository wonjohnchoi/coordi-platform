# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Post'
        db.create_table('general_post', (
            ('post_id', self.gf('django.db.models.fields.CharField')(default='dd8df7e22831afe496dfd677922664d2', max_length=32, primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.CustomUser'])),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 12, 25), auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 12, 25), auto_now=True, blank=True)),
            ('unique_visit', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('all_visit', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal('general', ['Post'])

        # Adding model 'Comment'
        db.create_table('general_comment', (
            ('comment_id', self.gf('django.db.models.fields.CharField')(default='cead01b25c38a2efac3cfed10c66b8e7', max_length=32, primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.CustomUser'])),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 12, 25), auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 12, 25), auto_now=True, blank=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Post'])),
        ))
        db.send_create_signal('general', ['Comment'])


    def backwards(self, orm):
        
        # Deleting model 'Post'
        db.delete_table('general_post')

        # Deleting model 'Comment'
        db.delete_table('general_comment')


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
        'general.album': {
            'Meta': {'object_name': 'Album'},
            'album_id': ('django.db.models.fields.CharField', [], {'default': "'533781ec498b3b1a24209ff2e4192d96'", 'max_length': '32', 'primary_key': 'True'}),
            'all_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.CustomUser']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 25)', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 25)', 'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title_photo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['general.TitlePhoto']", 'unique': 'True'}),
            'unique_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'general.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment_id': ('django.db.models.fields.CharField', [], {'default': "'5ed5a2365cda173c030243f819f94224'", 'max_length': '32', 'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.CustomUser']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['general.Post']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 25)', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 25)', 'auto_now': 'True', 'blank': 'True'})
        },
        'general.photo': {
            'Meta': {'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['general.Album']"}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_id': ('django.db.models.fields.CharField', [], {'default': "'ede9fccaf95af9d05be37ccd193c3c66'", 'max_length': '32', 'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'general.post': {
            'Meta': {'object_name': 'Post'},
            'all_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.CustomUser']"}),
            'post_id': ('django.db.models.fields.CharField', [], {'default': "'9ba0af44938176dba6edb4d9510ca34f'", 'max_length': '32', 'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 25)', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 25)', 'auto_now': 'True', 'blank': 'True'}),
            'unique_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'general.titlephoto': {
            'Meta': {'object_name': 'TitlePhoto'},
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_id': ('django.db.models.fields.CharField', [], {'default': "'25fd5fc089a1917880a041a4c5b6ed7d'", 'max_length': '32', 'primary_key': 'True'})
        },
        'registration.codi': {
            'Meta': {'object_name': 'Codi'},
            'birthday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'registration.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'accum_cach': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'accum_point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cash': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'codi': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.Codi']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['general']
