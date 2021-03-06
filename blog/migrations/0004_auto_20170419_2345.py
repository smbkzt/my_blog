# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170419_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='posted_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='post_body',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='post_article',
            new_name='title',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='preview',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Превью'),
            preserve_default=False,
        ),
    ]
