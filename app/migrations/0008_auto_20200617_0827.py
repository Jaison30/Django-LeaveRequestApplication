# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-06-17 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_employeedetails_total_no_of_leaves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]