# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0001_initial'),
        ('log_and_reg', '0006_auto_20170201_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='trips',
            field=models.ManyToManyField(to='travels.Travel'),
        ),
    ]
