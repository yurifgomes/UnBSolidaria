# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-16 00:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgposlogin', '0009_orgposlogin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orgposlogin',
            new_name='Solicitacao',
        ),
    ]
