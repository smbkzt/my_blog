# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.CharField(max_length=400),
        ),
    ]