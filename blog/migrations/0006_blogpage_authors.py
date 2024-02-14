# Generated by Django 5.0.2 on 2024-02-14 13:16

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="authors",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, to="blog.author"
            ),
        ),
    ]
