# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-26 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgposlogin', '0016_andamento_realizados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizados',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
