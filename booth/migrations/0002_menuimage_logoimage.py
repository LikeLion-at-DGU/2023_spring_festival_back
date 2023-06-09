# Generated by Django 4.2.1 on 2023-05-16 15:38

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("booth", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=core.models.image_upload_path
                    ),
                ),
                (
                    "booth",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="booth.booth"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="LogoImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=core.models.image_upload_path
                    ),
                ),
                (
                    "booth",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="booth.booth"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
