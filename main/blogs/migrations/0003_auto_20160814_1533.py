# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20160814_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.OneToOneField(default=0, to='blogs.Category'),
        ),
    ]
