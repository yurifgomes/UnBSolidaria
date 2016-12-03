# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unbsolidaria', '0002_andamento_realizados'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=120)),
                ('cep', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=240)),
                ('data_inicio', models.DateField(auto_now_add=True)),
                ('data_fim', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Andamento',
        ),
        migrations.DeleteModel(
            name='Realizados',
        ),
    ]