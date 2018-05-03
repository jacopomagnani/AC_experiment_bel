# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-03 05:26
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AcceptanceCurse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='side',
        ),
        migrations.RemoveField(
            model_name='player',
            name='wait',
        ),
        migrations.RemoveField(
            model_name='subsession',
            name='market_number',
        ),
        migrations.RemoveField(
            model_name='subsession',
            name='period',
        ),
        migrations.AddField(
            model_name='subsession',
            name='game',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
