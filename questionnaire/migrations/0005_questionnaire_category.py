# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20170713_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='category',
            field=models.CharField(choices=[('Cardiology_1', 'Cardiology_1'), ('Cardiology_2', 'Cardiology_2')], default=None, max_length=100, null=True, verbose_name='Please choose category of question'),
        ),
    ]
