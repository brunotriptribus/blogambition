# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160115_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default=0, null=True, upload_to=b'media/'),
        ),
    ]
