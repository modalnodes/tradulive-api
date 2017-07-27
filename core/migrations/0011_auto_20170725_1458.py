# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-25 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170725_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='translatorprofile',
            name='Nationality',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='bank',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='birth_city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='birth_country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='birth_day',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='cable_internet',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='cable_internet_provider',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='computer_model',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='fax',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='fuse',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='home_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='home_city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='home_country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='iban',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='id_card',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='mobile_internet',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='mobile_internet_provider',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='native_lang_1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='natives', to='core.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='native_lang_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_natives', to='core.Language'),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='passport',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='paypal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='secondary_mail',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='skype',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='soc_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='swift',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='tablet_model',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='tel_home',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='tel_model',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='tel_office',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='tel_private_cell',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='tel_work_cell',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='vat_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='vat_pic',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translatorprofile',
            name='video_pres',
            field=models.URLField(blank=True, null=True),
        ),
    ]