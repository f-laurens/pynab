# Generated by Django 3.2.12 on 2022-03-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nabsurprised", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="config",
            name="id",
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
    ]
