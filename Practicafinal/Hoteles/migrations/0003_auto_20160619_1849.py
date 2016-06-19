# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-19 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hoteles', '0002_remove_hotel_numcomentarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='imageSource',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='webSource',
        ),
        migrations.AddField(
            model_name='hotel',
            name='categoria',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='descripcion',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='estrellas',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='imageUrl',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='latitude',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='longitude',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='telefono',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='webUrl',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='direccion',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='nombreHotel',
            field=models.CharField(default='', max_length=200),
        ),
    ]
