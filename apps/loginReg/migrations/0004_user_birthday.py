# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg', '0003_auto_20170329_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
            preserve_default=False,
        ),
    ]
