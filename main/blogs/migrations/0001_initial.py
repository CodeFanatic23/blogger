# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields
import blogs.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('caption', models.CharField(max_length=300, null=True)),
                ('category', models.CharField(max_length=20, default='Others', blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('preview_image', models.ImageField(upload_to=blogs.models.upload_location, blank=True, null=True)),
                ('status', models.CharField(max_length=10, default='Draft', blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('title_slug', models.SlugField(editable=False)),
                ('preview_image_name', models.CharField(max_length=150, editable=False, null=True)),
                ('link_to_post', models.URLField(editable=False, null=True)),
            ],
        ),
    ]
