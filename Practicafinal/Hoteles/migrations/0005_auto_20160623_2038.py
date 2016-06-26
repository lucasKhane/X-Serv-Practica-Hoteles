# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hoteles', '0004_auto_20160621_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marcos', models.CharField(default='', max_length=200)),
                ('titulo', models.CharField(default='', max_length=200)),
                ('colordefondo', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='personalpage',
            old_name='titulo',
            new_name='tittlePage',
        ),
        migrations.RemoveField(
            model_name='personalpage',
            name='usuario',
        ),
        migrations.AddField(
            model_name='personalpage',
            name='user',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='personalpage',
            name='css',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hoteles.CSS'),
        ),
    ]