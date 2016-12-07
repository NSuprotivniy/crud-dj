# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=1)),
                ('address', models.CharField(max_length=200)),
                ('delivery_time', models.DateTimeField(verbose_name='delivery time')),
                ('status', models.CharField(default='delivering', max_length=20)),
            ],
        ),
    ]
