# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 21:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg', '0005_auto_20170329_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]
