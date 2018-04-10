# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20180410_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culture',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 25, 16, 39, 11, 488945)),
        ),
    ]
