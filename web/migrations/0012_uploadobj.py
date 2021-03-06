# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-14 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20171214_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadObj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=12)),
                ('b_author', models.CharField(max_length=12)),
                ('b_publisher', models.CharField(max_length=12)),
                ('b_description', models.CharField(max_length=12)),
                ('b_price', models.FloatField()),
                ('b_img', models.ImageField(upload_to=b'media')),
                ('b_way', models.IntegerField()),
            ],
        ),
    ]
