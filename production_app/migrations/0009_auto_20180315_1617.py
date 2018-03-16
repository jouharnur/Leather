# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production_app', '0008_auto_20180315_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cluster',
            options={},
        ),
        migrations.AlterField(
            model_name='member',
            name='network',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='production_app.Network', verbose_name='Network'),
        ),
    ]