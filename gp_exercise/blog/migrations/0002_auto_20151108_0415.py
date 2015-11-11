# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_text',
            field=models.TextField(default='Sample text ... , write your blog here', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='blog_image',
            field=models.ImageField(upload_to=b'blog_image/', blank=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='hero_image',
            field=models.ImageField(upload_to=b'hero_image/', blank=True),
        ),
    ]
