# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-26 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_backend_isimporting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backend',
            name='ntFileLastChange',
            field=models.CharField(blank=True, default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='backend',
            name='ntFilePath',
            field=models.CharField(blank=True, default='', max_length=600),
        ),
    ]
