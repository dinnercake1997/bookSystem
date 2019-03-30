# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-14 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20171214_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pictrue',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='state',
            field=models.IntegerField(blank=True, choices=[(0, 'on sale'), (1, 'sold'), (2, 'cancle')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
