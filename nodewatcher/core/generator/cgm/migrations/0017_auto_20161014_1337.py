# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-14 11:37
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import nodewatcher.core.registry.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0009_auto_20161013_1344'),
        ('cgm', '0016_auto_20160206_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwitchConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.IntegerField(editable=False, null=True)),
                ('annotations', jsonfield.fields.JSONField(default=dict, editable=False)),
                ('switch', nodewatcher.core.registry.fields.RegistryChoiceField(b'node.config', b'core.switch#switch', max_length=50)),
                ('vlan_preset', models.CharField(max_length=50)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_cgm.switchconfig_set+', to='contenttypes.ContentType')),
                ('root', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='config_cgm_switchconfig', to='core.Node')),
            ],
            options={
                'ordering': ['display_order', 'id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VLANConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.IntegerField(editable=False, null=True)),
                ('annotations', jsonfield.fields.JSONField(default=dict, editable=False)),
                ('name', models.CharField(max_length=30)),
                ('vlan', models.IntegerField()),
                ('ports', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_cgm.vlanconfig_set+', to='contenttypes.ContentType')),
                ('root', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='config_cgm_vlanconfig', to='core.Node')),
                ('switch', nodewatcher.core.registry.fields.IntraRegistryForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='vlans', to='cgm.SwitchConfig')),
            ],
            options={
                'ordering': ['display_order', 'id'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='allocatednetworkconfig',
            name='routing_announces',
            field=nodewatcher.core.registry.fields.RegistryMultipleChoiceField(base_field=models.CharField(choices=[(b'olsr', 'OLSR HNA'), (b'babel', 'Babel')], max_length=50), blank=True, default=list, enum_id=b'core.interfaces.network#routing_announce', null=True, regpoint=b'node.config', size=None, verbose_name='Announce Via'),
        ),
        migrations.AlterField(
            model_name='authenticationconfig',
            name='annotations',
            field=jsonfield.fields.JSONField(default=dict, editable=False),
        ),
        migrations.AlterField(
            model_name='bridgeinterfaceconfig',
            name='routing_protocols',
            field=nodewatcher.core.registry.fields.RegistryMultipleChoiceField(base_field=models.CharField(choices=[(b'olsr', 'OLSR'), (b'babel', 'Babel')], max_length=50), blank=True, default=list, enum_id=b'core.interfaces#routing_protocol', null=True, regpoint=b'node.config', size=None),
        ),
        migrations.AlterField(
            model_name='ethernetinterfaceconfig',
            name='eth_port',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ethernetinterfaceconfig',
            name='routing_protocols',
            field=nodewatcher.core.registry.fields.RegistryMultipleChoiceField(base_field=models.CharField(choices=[(b'olsr', 'OLSR'), (b'babel', 'Babel')], max_length=50), blank=True, default=list, enum_id=b'core.interfaces#routing_protocol', null=True, regpoint=b'node.config', size=None),
        ),
        migrations.AlterField(
            model_name='interfaceconfig',
            name='annotations',
            field=jsonfield.fields.JSONField(default=dict, editable=False),
        ),
        migrations.AlterField(
            model_name='networkconfig',
            name='annotations',
            field=jsonfield.fields.JSONField(default=dict, editable=False),
        ),
        migrations.AlterField(
            model_name='packageconfig',
            name='annotations',
            field=jsonfield.fields.JSONField(default=dict, editable=False),
        ),
        migrations.AlterField(
            model_name='staticnetworkconfig',
            name='routing_announces',
            field=nodewatcher.core.registry.fields.RegistryMultipleChoiceField(base_field=models.CharField(choices=[(b'olsr', 'OLSR HNA'), (b'babel', 'Babel')], max_length=50), blank=True, default=list, enum_id=b'core.interfaces.network#routing_announce', null=True, regpoint=b'node.config', size=None, verbose_name='Announce Via'),
        ),
        migrations.AlterField(
            model_name='wifiinterfaceconfig',
            name='bitrates',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='wifiinterfaceconfig',
            name='routing_protocols',
            field=nodewatcher.core.registry.fields.RegistryMultipleChoiceField(base_field=models.CharField(choices=[(b'olsr', 'OLSR'), (b'babel', 'Babel')], max_length=50), blank=True, default=list, enum_id=b'core.interfaces#routing_protocol', null=True, regpoint=b'node.config', size=None),
        ),
    ]