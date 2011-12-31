# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Vote'
        db.create_table('general_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.Theme'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.CustomUser'])),
        ))
        db.send_create_signal('general', ['Vote'])


    def backwards(self, orm):
        
        # Deleting model 'Vote'
        db.delete_table('general_vote')


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
            'album_id': ('django.db.models.fields.CharField', [], {'default': "'02867e80e81391f411b46461f7c100ab'", 'max_length': '32', 'primary_key': 'True'}),
            'all_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.CustomUser']"}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['general.Theme']", 'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 27)', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 27)', 'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title_photo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['general.TitlePhoto']", 'unique': 'True'}),
            'unique_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'general.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment_id': ('django.db.models.fields.CharField', [], {'default': "'f093019934b8396100f3eeafb693bcfd'", 'max_length': '32', 'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.CustomUser']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['general.Post']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 27)', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 27)', 'auto_now': 'True', 'blank': 'True'})
        },
        'general.photo': {
            'Meta': {'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['general.Album']"}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_id': ('django.db.models.fields.CharField', [], {'default': "'6f46a135dcd8eb7744565cec5a9bad37'", 'max_length': '32', 'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'general.post': {
            'Meta': {'object_name': 'Post'},
            'all_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.CustomUser']"}),
            'post_id': ('django.db.models.fields.CharField', [], {'default': "'137064769dd0df8f3956106f3f7d579d'", 'max_length': '32', 'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 27)', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2011, 12, 27)', 'auto_now': 'True', 'blank': 'True'}),
            'unique_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'general.theme': {
            'Meta': {'object_name': 'Theme'},
            'episode': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'season': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'general.titlephoto': {
            'Meta': {'object_name': 'TitlePhoto'},
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_id': ('django.db.models.fields.CharField', [], {'default': "'e4710bb2c88a57aa4697304249e65c17'", 'max_length': '32', 'primary_key': 'True'})
        },
        'general.vote': {
            'Meta': {'object_name': 'Vote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.CustomUser']"}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['general.Theme']"})
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
            'accum_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cash': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'codi': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.Codi']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'required_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['general']
