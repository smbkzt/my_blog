# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170420_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(blank=True, verbose_name='Дата публикации'),
        ),
    ]
