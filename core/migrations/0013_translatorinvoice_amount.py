# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-25 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_translatorinvoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='translatorinvoice',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]