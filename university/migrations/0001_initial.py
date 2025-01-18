# Generated by Django 5.1.1 on 2024-10-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("start_date", models.CharField(max_length=10)),
                ("end_date", models.CharField(max_length=10)),
                ("image", models.ImageField(blank=True, null=True, upload_to="course")),
            ],
        ),
        migrations.CreateModel(
            name="Enroll",
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
                ("course", models.CharField(max_length=255)),
                ("firstname", models.CharField(max_length=60)),
                ("lastname", models.CharField(max_length=60)),
                ("student_number", models.CharField(max_length=10)),
                ("phone", models.CharField(max_length=14)),
                ("major", models.CharField(max_length=255, null=True)),
                ("enrolled_at", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("published_at", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="news")),
            ],
        ),
    ]
