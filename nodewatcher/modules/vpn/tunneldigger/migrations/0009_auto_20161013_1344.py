# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-13 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import nodewatcher.core.registry.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vpn_tunneldigger', '0008_auto_20160206_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tunneldiggerbrokerconfig',
            name='routing_protocols',
            field=nodewatcher.core.registry.fields.RegistryMultipleChoiceField(base_field=models.CharField(choices=[(b'olsr', 'OLSR'), (b'babel', 'Babel')], max_length=50), blank=True, default=list, enum_id=b'core.interfaces#routing_protocol', null=True, regpoint=b'node.config', size=None),
        ),
        migrations.AlterField(
            model_name='tunneldiggerinterfaceconfig',
            name='routing_protocols',
            field=nodewatcher.core.registry.fields.RegistryMultipleChoiceField(base_field=models.CharField(choices=[(b'olsr', 'OLSR'), (b'babel', 'Babel')], max_length=50), blank=True, default=list, enum_id=b'core.interfaces#routing_protocol', null=True, regpoint=b'node.config', size=None),
        ),
    ]