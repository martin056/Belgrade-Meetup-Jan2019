# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-23 15:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.PositiveIntegerField(default=200)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='locations.Location')),
            ],
        ),
    ]
