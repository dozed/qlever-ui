# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-08 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backend',
            name='isDefault',
            field=models.BooleanField(default=0),
        ),
    ]
