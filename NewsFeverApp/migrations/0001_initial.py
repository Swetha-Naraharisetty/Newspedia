# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 06:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('a_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('a_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category', models.CharField(max_length=50)),
                ('c_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('m_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsFeverApp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.CharField(max_length=500)),
                ('image_url', models.CharField(max_length=100)),
                ('more_info', models.CharField(max_length=200)),
                ('public', models.IntegerField(default=1)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsFeverApp.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fname', models.CharField(max_length=100)),
                ('mname', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('lname', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('is_self_ratting', models.BooleanField(default=False)),
                ('is_registered', models.BooleanField(default=False)),
                ('is_pwd_reset', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('p_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('category', models.CharField(max_length=50)),
                ('s_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='publisher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsFeverApp.Publisher'),
        ),
        migrations.AddField(
            model_name='news',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mapping',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsFeverApp.SubCategory'),
        ),
    ]
