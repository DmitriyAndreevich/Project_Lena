# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modern_cv', '0005_posts_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='image',
            new_name='big_image',
        ),
        migrations.AddField(
            model_name='projects',
            name='small_image',
            field=models.ImageField(blank=True, max_length=75, upload_to=''),
        ),
    ]
