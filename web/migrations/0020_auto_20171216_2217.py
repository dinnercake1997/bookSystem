# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-16 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20171216_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
