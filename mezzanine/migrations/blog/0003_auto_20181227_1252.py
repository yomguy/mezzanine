# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-27 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180307_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='_meta_title',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Meta title'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='_meta_title_en',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Meta title'),
        ),
    ]
