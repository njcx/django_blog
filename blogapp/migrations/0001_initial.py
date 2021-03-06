# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('article_name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('release', models.BooleanField()),
            ],
            options={
                'ordering': ['-create_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('user_name', models.CharField(max_length=100)),
                ('qq', models.IntegerField()),
                ('wechat', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ['-create_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('user_name', models.CharField(max_length=100)),
                ('qq', models.IntegerField()),
                ('wechat', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('ip', models.GenericIPAddressField()),
            ],
            options={
                'ordering': ['-create_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('kw', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('qq', models.CharField(max_length=30)),
                ('wechat', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
    ]
