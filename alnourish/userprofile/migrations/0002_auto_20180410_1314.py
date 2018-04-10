# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='culture',
            name='ph_test',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='culture',
            name='test_date',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
