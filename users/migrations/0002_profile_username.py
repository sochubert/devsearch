# Generated by Django 4.1.6 on 2023-02-12 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="username",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
