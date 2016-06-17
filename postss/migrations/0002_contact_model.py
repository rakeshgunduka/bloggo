# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('emailid', models.EmailField(max_length=120)),
                ('contact_no', models.IntegerField()),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
