# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callout', '0008_auto_20160427_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='beacons',
            field=models.ManyToManyField(blank=True, related_name='workspaces', to='callout.Beacon'),
        ),
    ]
