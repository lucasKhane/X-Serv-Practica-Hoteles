# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hoteles', '0011_hotel_firstfoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='numcomentarios',
            field=models.IntegerField(default=0),
        ),
    ]
