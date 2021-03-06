# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield


class Migration(migrations.Migration):

    dependencies = [
        ('sensors_generic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericsensormonitor',
            name='annotations',
            field=jsonfield.JSONField(default={}, help_text='Enter a valid JSON object', editable=False),
        ),
    ]
