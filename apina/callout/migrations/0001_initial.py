# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(blank=True, max_length=60)),
                ('minor', models.CharField(blank=True, max_length=60)),
                ('uuid', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(1, 'Attendee'), (2, 'Admin')], default=1)),
                ('feedback', models.CharField(blank=True, max_length=1000)),
                ('status', models.CharField(choices=[('F', 'Following'), ('U', 'Unsure'), ('R', 'Requesting assistance')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_starting', models.DateField(blank=True)),
                ('date_ending', models.DateField(blank=True)),
                ('name', models.CharField(max_length=50)),
                ('beacons', models.ManyToManyField(blank=True, to='callout.Beacon')),
            ],
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callout.User'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callout.Workspace'),
        ),
    ]
