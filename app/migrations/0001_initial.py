# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1024)),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.BooleanField(default=False)),
                ('answered', models.BooleanField(default=False)),
                ('uuid', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('decision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Decision')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('decision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Decision')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=62)),
            ],
        ),
        migrations.CreateModel(
            name='WeightedCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Criteria')),
                ('invitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Invitation')),
            ],
        ),
        migrations.AddField(
            model_name='invitation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='criteria',
            name='decision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Decision'),
        ),
        migrations.AddField(
            model_name='answer',
            name='criteria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Criteria'),
        ),
        migrations.AddField(
            model_name='answer',
            name='invitation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Invitation'),
        ),
        migrations.AddField(
            model_name='answer',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Option'),
        ),
    ]
