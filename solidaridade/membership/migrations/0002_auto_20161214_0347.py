# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-14 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='birth_date',
        ),
        migrations.AlterField(
            model_name='member',
            name='subscription_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='subscription date'),
        ),
    ]
