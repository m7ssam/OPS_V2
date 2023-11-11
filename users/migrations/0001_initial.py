# Generated by Django 4.2.5 on 2023-11-11 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User_id",
            fields=[
                (
                    "id",
                    models.CharField(max_length=7, primary_key=True, serialize=False),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("middle_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
    ]