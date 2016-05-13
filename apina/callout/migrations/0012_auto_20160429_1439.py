# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('callout', '0011_workspace_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callout.User'),
        ),
    ]