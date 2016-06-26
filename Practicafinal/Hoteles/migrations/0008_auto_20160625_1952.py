# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-25 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hoteles', '0007_auto_20160625_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='numComentarios',
        ),
        migrations.AddField(
            model_name='comentario',
            name='hotel',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hoteles.Hotel'),
        ),
    ]
