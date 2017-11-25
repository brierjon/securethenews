# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 02:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0019_sitecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='sitecategory',
            field=models.ForeignKey(blank=True, help_text='Select which leaderboard you would like this news site to appear on', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='sites.SiteCategory'),
        ),
    ]