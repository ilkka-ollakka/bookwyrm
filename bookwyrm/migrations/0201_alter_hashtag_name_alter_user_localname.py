# Generated by Django 4.2.11 on 2024-04-01 21:09

import bookwyrm.models.fields
from django.db import migrations, models
from django.contrib.postgres.operations import CreateCollation


class Migration(migrations.Migration):
    dependencies = [
        ("bookwyrm", "0200_alter_user_preferred_timezone"),
    ]

    operations = [
        CreateCollation(
            "case_insensitive",
            provider="icu",
            locale="und-u-ks-level2",
            deterministic=False,
        ),
        migrations.AlterField(
            model_name="hashtag",
            name="name",
            field=bookwyrm.models.fields.CharField(
                db_collation="case_insensitive", max_length=256
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="localname",
            field=models.CharField(
                max_length=255,
                null=True,
                unique=False,
                validators=[bookwyrm.models.fields.validate_localname],
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="localname",
            field=models.CharField(
                db_collation="case_insensitive",
                max_length=255,
                null=True,
                unique=True,
                validators=[bookwyrm.models.fields.validate_localname],
            ),
        ),
    ]
