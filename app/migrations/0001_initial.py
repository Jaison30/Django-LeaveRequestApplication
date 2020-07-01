# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-06-13 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('no_of_leaves', models.PositiveIntegerField(default=0)),
                ('no_of_remaining_leaves', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_leaves', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('no_of_days', models.PositiveIntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('status', models.CharField(choices=[('Not Approved', 'Not Approved'), ('Approved', 'Approved')], default='Not Approved', max_length=20)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='app.EmployeeDetails')),
            ],
        ),
    ]
