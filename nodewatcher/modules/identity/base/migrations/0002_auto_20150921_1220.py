# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield


class Migration(migrations.Migration):

    dependencies = [
        ('identity_base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='identityconfig',
            name='annotations',
            field=jsonfield.JSONField(default={}, help_text='Enter a valid JSON object', editable=False),
        ),
        migrations.AddField(
            model_name='identitymechanismconfig',
            name='annotations',
            field=jsonfield.JSONField(default={}, help_text='Enter a valid JSON object', editable=False),
        ),
    ]
