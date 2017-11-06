# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-09 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20170920_0511'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslatorAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dow', models.IntegerField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('removed', models.DateTimeField()),
                ('translator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='core.TranslatorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TranslatorAvailabilityException',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('removed', models.DateTimeField()),
                ('date', models.DateField()),
                ('translator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exceptions', to='core.TranslatorProfile')),
            ],
        ),
        migrations.AlterField(
            model_name='translatormicrovoc',
            name='microvoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='core.MicroVocabulary'),
        ),
    ]