# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 19:53
from __future__ import unicode_literals

from django.db import migrations
import draceditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blogpost_html_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=draceditor.models.DraceditorField(),
        ),
    ]
