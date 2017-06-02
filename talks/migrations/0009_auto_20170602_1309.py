# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-02 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0008_auto_20170602_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='experience_level',
            field=models.CharField(choices=[('Beginner', 'Beginner, no prior knowledge of Python required'), ('Mid-level Programmers', 'Average, some prior knowledge of Python required'), ('Senior Programmers', 'Good Python programmers level'), ('Expert Programmers', 'Experienced Python programmers level')], default='', max_length=30),
        ),
    ]
