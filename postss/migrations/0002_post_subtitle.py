# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-14 07:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default=datetime.datetime(2016, 6, 14, 7, 37, 4, 856182, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]