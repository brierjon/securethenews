# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 21:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0017_auto_20161105_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pledge',
            old_name='status',
            new_name='review_status',
        ),
    ]
