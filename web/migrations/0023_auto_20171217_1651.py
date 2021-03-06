# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-17 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_auto_20171217_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='s_b',
            old_name='buyer_name',
            new_name='book_id',
        ),
        migrations.RenameField(
            model_name='s_b',
            old_name='seller_name',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='s_b',
            name='comment',
        ),
        migrations.AddField(
            model_name='order',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tobuyer_anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='tobuyer_score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='s_b',
            name='relation',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
