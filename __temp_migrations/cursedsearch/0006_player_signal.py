# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-06 10:20
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cursedsearch', '0005_remove_player_signal'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='signal',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
