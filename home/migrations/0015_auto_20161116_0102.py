# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 01:02
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20161115_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock()), ('source', wagtail.wagtailcore.blocks.CharBlock()), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))), ('table', wagtail.contrib.table_block.blocks.TableBlock()))),
        ),
    ]
