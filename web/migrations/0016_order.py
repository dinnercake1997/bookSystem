# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-16 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20171216_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(blank=True, max_length=20, null=True)),
                ('buyer_name', models.CharField(blank=True, max_length=20, null=True)),
                ('book_id', models.CharField(blank=True, max_length=20, null=True)),
                ('bookname', models.CharField(blank=True, max_length=20, null=True)),
                ('picture', models.ImageField(blank=True, default='logo.png', null=True, upload_to='')),
                ('price', models.FloatField(blank=True, max_length=24, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, default='None', max_length=200, null=True)),
                ('state', models.IntegerField(blank=True, choices=[(0, 'buy'), (1, 'collect')], default=0, null=True)),
            ],
        ),
    ]
