# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-26 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form_automation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestdetails',
            name='request_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
