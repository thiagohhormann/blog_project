# Generated by Django 5.1 on 2024-10-30 13:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
