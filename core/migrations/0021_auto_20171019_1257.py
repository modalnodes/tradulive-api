# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-19 12:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20171010_0647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translatoravailabilityexception',
            old_name='date',
            new_name='date_from',
        ),
        migrations.AddField(
            model_name='translatoravailabilityexception',
            name='date_to',
            field=models.DateField(default=datetime.datetime(2017, 10, 19, 12, 57, 48, 697962, tzinfo=utc)),
            preserve_default=False,
        ),
    ]