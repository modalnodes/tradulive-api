# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-06 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20171019_1257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='translatoravailability',
            options={'ordering': ['dow']},
        ),
    ]
