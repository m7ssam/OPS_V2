# Generated by Django 4.2.5 on 2023-11-06 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
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
                    "photo",
                    models.ImageField(
                        default="static\\images\\Project\\Cover\\default.jpg",
                        upload_to="media/project/<django.db.models.fields.related.ForeignKey>",
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="project.name"
                    ),
                ),
            ],
        ),
    ]