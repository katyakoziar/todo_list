# Generated by Django 4.2.7 on 2023-11-27 12:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["is_completed", "-created_at"]},
        ),
    ]
