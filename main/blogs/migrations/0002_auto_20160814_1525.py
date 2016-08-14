# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='preview_image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='blogauthor',
            field=models.CharField(blank=True, max_length=20, default='dopy', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='blogauthor_slug',
            field=models.SlugField(editable=False, default=1),
            preserve_default=False,
        ),
    ]
