# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-25 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hoteles', '0006_auto_20160624_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=200)),
                ('date', models.DateField(default='')),
                ('contenido', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='numComentarios',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotel',
            name='comentario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hoteles.Comentario'),
        ),
    ]
