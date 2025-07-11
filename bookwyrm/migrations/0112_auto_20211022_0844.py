# Generated by Django 3.2.5 on 2021-10-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0111_merge_0107_auto_20211016_0639_0110_auto_20211015_1734"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="notification",
            name="notification_type_valid",
        ),
        migrations.AlterField(
            model_name="notification",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("FAVORITE", "Favorite"),
                    ("REPLY", "Reply"),
                    ("MENTION", "Mention"),
                    ("TAG", "Tag"),
                    ("FOLLOW", "Follow"),
                    ("FOLLOW_REQUEST", "Follow Request"),
                    ("BOOST", "Boost"),
                    ("IMPORT", "Import"),
                    ("ADD", "Add"),
                    ("REPORT", "Report"),
                    ("INVITE", "Invite"),
                    ("ACCEPT", "Accept"),
                    ("JOIN", "Join"),
                    ("LEAVE", "Leave"),
                    ("REMOVE", "Remove"),
                    ("GROUP_PRIVACY", "Group Privacy"),
                    ("GROUP_NAME", "Group Name"),
                    ("GROUP_DESCRIPTION", "Group Description"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="preferred_language",
            field=models.CharField(
                blank=True,
                choices=[
                    ("en-us", "English"),
                    ("de-de", "Deutsch (German)"),
                    ("es-es", "Español (Spanish)"),
                    ("fr-fr", "Français (French)"),
                    ("pt-br", "Português - Brasil (Brazilian Portuguese)"),
                    ("zh-hans", "简体中文 (Simplified Chinese)"),
                    ("zh-hant", "繁體中文 (Traditional Chinese)"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddConstraint(
            model_name="notification",
            constraint=models.CheckConstraint(
                condition=models.Q(
                    (
                        "notification_type__in",
                        [
                            "FAVORITE",
                            "REPLY",
                            "MENTION",
                            "TAG",
                            "FOLLOW",
                            "FOLLOW_REQUEST",
                            "BOOST",
                            "IMPORT",
                            "ADD",
                            "REPORT",
                            "INVITE",
                            "ACCEPT",
                            "JOIN",
                            "LEAVE",
                            "REMOVE",
                            "GROUP_PRIVACY",
                            "GROUP_NAME",
                            "GROUP_DESCRIPTION",
                        ],
                    )
                ),
                name="notification_type_valid",
            ),
        ),
    ]
