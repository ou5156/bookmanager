# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2019-12-31 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
    ]