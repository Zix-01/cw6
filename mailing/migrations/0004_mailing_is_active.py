# Generated by Django 4.2.2 on 2024-11-18 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0003_alter_mailing_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]