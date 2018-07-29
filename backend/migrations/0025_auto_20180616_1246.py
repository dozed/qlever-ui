# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_auto_20180609_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backend',
            name='dynamicSuggestions',
            field=models.IntegerField(choices=[(2, '3. Dynamic backend suggestions (pre-evaluation)'), (1, '2. Suggestions based on position and backend'), (0, '1. SPARQL syntax only')], default=True, help_text='If you want to disable the dynamic suggestions from QLever or QLever UI by default change this option.', verbose_name='Default suggestion mode'),
        ),
    ]
