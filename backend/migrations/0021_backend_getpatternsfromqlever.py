# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-18 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_example_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='backend',
            name='getPatternsFromQLever',
            field=models.BooleanField(default=False),
        ),
    ]
