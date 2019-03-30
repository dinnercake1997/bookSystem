# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-14 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_user_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pictrue',
            field=models.ImageField(blank=True, null=True, upload_to='b_img'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='u_img'),
        ),
    ]