# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-11 13:08
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('crt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='num_correct',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
