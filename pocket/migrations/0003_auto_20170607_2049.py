# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 13:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pocket', '0002_auto_20170607_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pocket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
