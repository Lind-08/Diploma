# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-19 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config_app', '0002_auto_20160419_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
    ]
