# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpost_html_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='html_field',
        ),
    ]
