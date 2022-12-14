# Generated by Django 4.1.1 on 2022-09-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stealMyBrain", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("phone", models.IntegerField()),
                ("email", models.EmailField(max_length=50)),
                ("age", models.IntegerField()),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("APP", "Apprentice"),
                            ("TR", "Trainee"),
                            ("JR", "Junior"),
                            ("SNR", "Senior"),
                            ("LD", "Lead"),
                            ("HD", "Head"),
                        ],
                        max_length=4,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Supervisor",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
            ],
        ),
    ]
