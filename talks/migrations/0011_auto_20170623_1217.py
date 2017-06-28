# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-23 12:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('talks', '0010_auto_20170602_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(verbose_name='content of the email')),
                ('recipient_group', models.CharField(choices=[('Keynote', 'Keynote Talk - 45 mins'), ('Short Talk', 'Short Talk - 30 mins'), ('Long Talk', 'Long Talk - 1 hour'), ('Tutorial', 'Tutorial - 2 hours or more')], max_length=50)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='proposal',
            name='proposal',
            field=models.CharField(default='', max_length=255),
        ),
    ]