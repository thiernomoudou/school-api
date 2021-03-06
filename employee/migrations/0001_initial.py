# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), (None, 'Select gender')], max_length=32)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('adress', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=32)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('id_card_number', models.CharField(max_length=64)),
                ('job_type', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('ssn', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.Employee')),
                ('title', models.CharField(max_length=100)),
            ],
            bases=('employee.employee',),
        ),
    ]
