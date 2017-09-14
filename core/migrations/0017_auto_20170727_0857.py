# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-27 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20170727_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='translatorprofile',
            name='fuse',
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='home_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='home_city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='home_country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='secondary_mail',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='skype',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='tel_home',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='tel_office',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='tel_private_cell',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='tel_work_cell',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='tel_home',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customeruser',
            name='tel_office',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='fax',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='translatorprofile',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PersonTitle'),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PersonTitle'),
        ),
    ]