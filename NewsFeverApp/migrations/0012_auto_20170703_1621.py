# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeverApp', '0011_auto_20170703_1617'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SourceCategoryMapping',
            new_name='SourceCategoryMap',
        ),
    ]