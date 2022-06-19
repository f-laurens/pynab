# Generated by Django 3.2.13 on 2022-06-04 21:53

from django.db import migrations, models

import nabweatherd.models


class Migration(migrations.Migration):

    dependencies = [
        ("nabweatherd", "0013_alter_config_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="config",
            name="location",
        ),
        migrations.AddField(
            model_name="config",
            name="location",
            field=models.JSONField(
                default=nabweatherd.models.default_location, null=True
            ),
        ),
    ]
