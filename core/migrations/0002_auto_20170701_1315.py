# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-01 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='value',
            field=models.FloatField(default=0),
        ),
    ]