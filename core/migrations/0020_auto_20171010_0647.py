# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-10 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20171009_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translatoravailability',
            name='removed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='translatoravailabilityexception',
            name='removed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
