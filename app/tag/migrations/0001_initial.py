# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, max_length=512, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='date updated')),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]