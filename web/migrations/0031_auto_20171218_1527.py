# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-18 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_auto_20171218_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, default=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='book_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='bookname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer_id',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='order',
            name='picture',
            field=models.ImageField(default='logo.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(max_length=24),
        ),
        migrations.AlterField(
            model_name='order',
            name='seller_id',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.IntegerField(choices=[(0, 'buy'), (1, 'cancle')], default=0),
        ),
    ]
