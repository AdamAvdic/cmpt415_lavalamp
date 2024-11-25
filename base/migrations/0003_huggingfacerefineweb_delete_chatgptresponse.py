# Generated by Django 5.1.1 on 2024-11-25 01:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_chatgptresponse_delete_bubblewords"),
    ]

    operations = [
        migrations.CreateModel(
            name="HuggingFaceRefineWeb",
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
                ("content", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="ChatGPTResponse",
        ),
    ]