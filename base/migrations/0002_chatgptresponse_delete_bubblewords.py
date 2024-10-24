# Generated by Django 5.1.1 on 2024-10-21 21:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatGPTResponse",
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
                ("response", models.TextField()),
            ],
            options={
                "db_table": "chatgptresponse",
            },
        ),
        migrations.DeleteModel(
            name="BubbleWords",
        ),
    ]
