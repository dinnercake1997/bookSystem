# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-18 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_auto_20171218_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='way',
            field=models.IntegerField(blank=True, choices=[(0, 'cancle'), (1, '面交'), (2, '快递'), (3, '面交或快递')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(blank=True, default='None', max_length=40, null=True),
        ),
    ]