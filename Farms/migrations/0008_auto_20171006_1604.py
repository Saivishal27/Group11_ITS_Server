# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farms', '0007_farm_farm_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season_wise_crop',
            name='crop_id',
        ),
        migrations.AddField(
            model_name='season_wise_crop',
            name='crop_name',
            field=models.CharField(default='Rice', max_length=20),
        ),
    ]
