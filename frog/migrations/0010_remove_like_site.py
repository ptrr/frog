# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-15 03:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frog', '0009_auto_20170707_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='site',
        ),
    ]
