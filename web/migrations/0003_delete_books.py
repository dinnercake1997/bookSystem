# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-06 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_books'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Books',
        ),
    ]
