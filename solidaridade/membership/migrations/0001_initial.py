# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-23 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, max_length=500, null=True, verbose_name='note')),
                ('sum', models.PositiveIntegerField(verbose_name='sum')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='due date')),
                ('paid', models.BooleanField(default=False, verbose_name='paid')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='payment date')),
                ('payment_method', models.CharField(blank=True, choices=[('paypal', 'Paypal'), ('check', 'check'), ('cash', 'cash'), ('natural', 'natural'), ('bank-transfer', 'bank transfer'), ('electronic', 'electronic payment')], max_length=20, null=True, verbose_name='payment method')),
            ],
            options={
                'verbose_name': 'contribution',
                'verbose_name_plural': 'contributions',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('birth_date', models.DateField(verbose_name='birth date')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='country')),
                ('address', models.TextField(max_length=300, verbose_name='address')),
                ('postal_code', models.CharField(max_length=20, verbose_name='postal code')),
                ('city', models.CharField(max_length=70, verbose_name='city')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subscription_date', models.DateField(verbose_name='subscription date')),
                ('validated', models.BooleanField(default=False, verbose_name='validated')),
                ('validation_date', models.DateField(blank=True, null=True, verbose_name='validation date')),
                ('unsubscripted', models.BooleanField(default=False, verbose_name='unsubscripted')),
                ('unsubscription_date', models.DateField(blank=True, null=True, verbose_name='unsubscription date')),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(max_length=300, verbose_name='description')),
                ('entry_fees', models.PositiveIntegerField(verbose_name='entry fees')),
                ('monthly_contribution', models.PositiveIntegerField(verbose_name='monthly contribution')),
            ],
            options={
                'verbose_name': 'title',
                'verbose_name_plural': 'titles',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.Title'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.Member', verbose_name='member'),
        ),
    ]
