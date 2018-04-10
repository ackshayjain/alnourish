# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20180410_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='culture',
            old_name='date_published',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='culture',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 25, 13, 29, 18, 208189)),
        ),
    ]
