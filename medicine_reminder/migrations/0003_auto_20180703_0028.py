# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-02 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_reminder', '0002_auto_20180703_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminderdataforparticularmed',
            name='medicine_id',
        ),
        migrations.AddField(
            model_name='reminderdataforparticularmed',
            name='medicine_id',
            field=models.ManyToManyField(to='medicine_reminder.Medicine'),
        ),
    ]
