# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-17 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_auto_20171217_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tobuyer_c_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='tobuyer_comment',
            field=models.IntegerField(blank=True, default='None', max_length=200, null=True),
        ),
    ]