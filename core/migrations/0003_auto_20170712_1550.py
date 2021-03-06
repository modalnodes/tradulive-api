# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-12 15:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20170701_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='language',
        ),
        migrations.AddField(
            model_name='appointment',
            name='credits',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='customer_language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer_lang_requests', to='core.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='other_language',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='other_lang_requests', to='core.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='requester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointmentclosure',
            name='closer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certification',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Language'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='core.CustomerProfile'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='translator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='core.TranslatorProfile'),
        ),
        migrations.AlterField(
            model_name='appointmentclosure',
            name='closure_reason',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='core.CustomerProfile'),
        ),
        migrations.AddField(
            model_name='creditassignment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='core.CustomerProfile'),
        ),
        migrations.AddField(
            model_name='creditassignment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
