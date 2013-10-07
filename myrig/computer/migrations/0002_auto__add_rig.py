# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rig'
        db.create_table(u'computer_rig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('computer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['computer.Computer'])),
        ))
        db.send_create_signal(u'computer', ['Rig'])


    def backwards(self, orm):
        # Deleting model 'Rig'
        db.delete_table(u'computer_rig')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'computer.chipset': {
            'Meta': {'object_name': 'Chipset', '_ormbases': [u'computer.Component']},
            u'component_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['computer.Component']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'computer.component': {
            'Meta': {'object_name': 'Component'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['computer.Manufacturer']"}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'computer.computer': {
            'Meta': {'object_name': 'Computer'},
            'chipset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['computer.Chipset']", 'null': 'True', 'blank': 'True'}),
            'hard_drives': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['computer.HardDrive']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memory': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['computer.Memory']", 'null': 'True', 'blank': 'True'}),
            'operating_systems': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['computer.OperatingSystem']", 'null': 'True', 'blank': 'True'}),
            'processors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['computer.Processor']", 'null': 'True', 'blank': 'True'}),
            'video_adapters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['computer.VideoAdapter']", 'null': 'True', 'blank': 'True'})
        },
        u'computer.harddrive': {
            'Meta': {'object_name': 'HardDrive', '_ormbases': [u'computer.Component']},
            u'component_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['computer.Component']", 'unique': 'True', 'primary_key': 'True'}),
            'size': ('myrig.computer.models.SIIntegerField', [], {'unit': "'B'"}),
            'ssd': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'computer.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'computer.memory': {
            'Meta': {'object_name': 'Memory', '_ormbases': [u'computer.Component']},
            u'component_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['computer.Component']", 'unique': 'True', 'primary_key': 'True'}),
            'size': ('myrig.computer.models.SIIntegerField', [], {'unit': "'B'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'computer.operatingsystem': {
            'Meta': {'object_name': 'OperatingSystem'},
            'architecture': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'computer.processor': {
            'Meta': {'object_name': 'Processor', '_ormbases': [u'computer.Component']},
            'clock_speed': ('myrig.computer.models.SIIntegerField', [], {'unit': "'Hz'"}),
            u'component_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['computer.Component']", 'unique': 'True', 'primary_key': 'True'}),
            'cores': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        u'computer.rig': {
            'Meta': {'object_name': 'Rig'},
            'computer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['computer.Computer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'computer.videoadapter': {
            'Meta': {'object_name': 'VideoAdapter', '_ormbases': [u'computer.Component']},
            u'component_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['computer.Component']", 'unique': 'True', 'primary_key': 'True'}),
            'memory': ('myrig.computer.models.SIIntegerField', [], {'unit': "'B'"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['computer']