# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-12 11:32
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
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cell_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threadible_app.Cell')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WSUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_execute', models.BooleanField()),
                ('can_write', models.BooleanField()),
                ('is_admin', models.BooleanField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workspace_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threadible_app.Workspace')),
            ],
        ),
        migrations.AddField(
            model_name='cell',
            name='workspace_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threadible_app.Workspace'),
        ),
    ]
