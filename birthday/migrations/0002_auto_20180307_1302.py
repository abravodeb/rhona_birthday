# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 16:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cumple',
            new_name='BirthdayDay',
        ),
        migrations.RenameModel(
            old_name='Mensaje',
            new_name='BirthdayMessage',
        ),
        migrations.RenameField(
            model_name='birthdayday',
            old_name='cumple',
            new_name='birthday_day',
        ),
        migrations.RenameField(
            model_name='birthdayday',
            old_name='nombre',
            new_name='name',
        ),
    ]
