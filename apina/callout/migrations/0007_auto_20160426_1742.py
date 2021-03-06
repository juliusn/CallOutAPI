# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('callout', '0006_auto_20160426_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='callout.Subscription'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='callout.User'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='beacons',
            field=models.ManyToManyField(blank=True, related_name='workspaces', to='callout.Beacon'),
        ),
    ]
