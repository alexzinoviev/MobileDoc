# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_remove_questionnaire_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='answer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=1, null=True, verbose_name='Do you?'),
        ),
    ]
