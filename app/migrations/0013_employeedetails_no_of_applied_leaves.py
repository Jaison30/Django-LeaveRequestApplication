# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-07-06 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200619_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='no_of_applied_leaves',
            field=models.FloatField(default=0),
        ),
    ]
