# Generated by Django 4.2.2 on 2023-06-10 14:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("specialists", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="specialists",
            options={
                "verbose_name": "специалист",
                "verbose_name_plural": "специалисты",
            },
        ),
    ]
