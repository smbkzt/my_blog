# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170420_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='html_field',
            field=models.TextField(default='x', editable=False),
            preserve_default=False,
        ),
    ]