# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manufacturer'
        db.create_table(u'computer_manufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'computer', ['Manufacturer'])

        # Adding model 'Component'
        db.create_table(u'computer_component', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['computer.Manufacturer'])),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'computer', ['Component'])

        # Adding model 'Chipset'
        db.create_table(u'computer_chipset', (
            (u'component_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['computer.Component'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'computer', ['Chipset'])

        # Adding model 'Processor'
        db.create_table(u'computer_processor', (
            (u'component_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['computer.Component'], unique=True, primary_key=True)),
            ('series', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('clock_speed', self.gf('myrig.computer.models.SIIntegerField')(unit='Hz')),
            ('cores', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'computer', ['Processor'])

        # Adding model 'Memory'
        db.create_table(u'computer_memory', (
            (u'component_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['computer.Component'], unique=True, primary_key=True)),
            ('size', self.gf('myrig.computer.models.SIIntegerField')(unit='B')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'computer', ['Memory'])

        # Adding model 'HardDrive'
        db.create_table(u'computer_harddrive', (
            (u'component_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['computer.Component'], unique=True, primary_key=True)),
            ('size', self.gf('myrig.computer.models.SIIntegerField')(unit='B')),
            ('ssd', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'computer', ['HardDrive'])

        # Adding model 'VideoAdapter'
        db.create_table(u'computer_videoadapter', (
            (u'component_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['computer.Component'], unique=True, primary_key=True)),
            ('memory', self.gf('myrig.computer.models.SIIntegerField')(unit='B')),
        ))
        db.send_create_signal(u'computer', ['VideoAdapter'])

        # Adding model 'OperatingSystem'
        db.create_table(u'computer_operatingsystem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('architecture', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'computer', ['OperatingSystem'])

        # Adding model 'Computer'
        db.create_table(u'computer_computer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chipset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['computer.Chipset'], null=True, blank=True)),
        ))
        db.send_create_signal(u'computer', ['Computer'])

        # Adding M2M table for field processors on 'Computer'
        m2m_table_name = db.shorten_name(u'computer_computer_processors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('computer', models.ForeignKey(orm[u'computer.computer'], null=False)),
            ('processor', models.ForeignKey(orm[u'computer.processor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['computer_id', 'processor_id'])

        # Adding M2M table for field memory on 'Computer'
        m2m_table_name = db.shorten_name(u'computer_computer_memory')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('computer', models.ForeignKey(orm[u'computer.computer'], null=False)),
            ('memory', models.ForeignKey(orm[u'computer.memory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['computer_id', 'memory_id'])

        # Adding M2M table for field hard_drives on 'Computer'
        m2m_table_name = db.shorten_name(u'computer_computer_hard_drives')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('computer', models.ForeignKey(orm[u'computer.computer'], null=False)),
            ('harddrive', models.ForeignKey(orm[u'computer.harddrive'], null=False))
        ))
        db.create_unique(m2m_table_name, ['computer_id', 'harddrive_id'])

        # Adding M2M table for field video_adapters on 'Computer'
        m2m_table_name = db.shorten_name(u'computer_computer_video_adapters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('computer', models.ForeignKey(orm[u'computer.computer'], null=False)),
            ('videoadapter', models.ForeignKey(orm[u'computer.videoadapter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['computer_id', 'videoadapter_id'])

        # Adding M2M table for field operating_systems on 'Computer'
        m2m_table_name = db.shorten_name(u'computer_computer_operating_systems')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('computer', models.ForeignKey(orm[u'computer.computer'], null=False)),
            ('operatingsystem', models.ForeignKey(orm[u'computer.operatingsystem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['computer_id', 'operatingsystem_id'])


    def backwards(self, orm):
        # Deleting model 'Manufacturer'
        db.delete_table(u'computer_manufacturer')

        # Deleting model 'Component'
        db.delete_table(u'computer_component')

        # Deleting model 'Chipset'
        db.delete_table(u'computer_chipset')

        # Deleting model 'Processor'
        db.delete_table(u'computer_processor')

        # Deleting model 'Memory'
        db.delete_table(u'computer_memory')

        # Deleting model 'HardDrive'
        db.delete_table(u'computer_harddrive')

        # Deleting model 'VideoAdapter'
        db.delete_table(u'computer_videoadapter')

        # Deleting model 'OperatingSystem'
        db.delete_table(u'computer_operatingsystem')

        # Deleting model 'Computer'
        db.delete_table(u'computer_computer')

        # Removing M2M table for field processors on 'Computer'
        db.delete_table(db.shorten_name(u'computer_computer_processors'))

        # Removing M2M table for field memory on 'Computer'
        db.delete_table(db.shorten_name(u'computer_computer_memory'))

        # Removing M2M table for field hard_drives on 'Computer'
        db.delete_table(db.shorten_name(u'computer_computer_hard_drives'))

        # Removing M2M table for field video_adapters on 'Computer'
        db.delete_table(db.shorten_name(u'computer_computer_video_adapters'))

        # Removing M2M table for field operating_systems on 'Computer'
        db.delete_table(db.shorten_name(u'computer_computer_operating_systems'))


    models = {
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
        u'computer.videoadapter': {
            'Meta': {'object_name': 'VideoAdapter', '_ormbases': [u'computer.Component']},
            u'component_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['computer.Component']", 'unique': 'True', 'primary_key': 'True'}),
            'memory': ('myrig.computer.models.SIIntegerField', [], {'unit': "'B'"})
        }
    }

    complete_apps = ['computer']