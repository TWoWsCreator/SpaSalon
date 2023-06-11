# Generated by Django 4.2.2 on 2023-06-10 22:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reception", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reception",
            name="mail",
            field=models.EmailField(
                blank=True,
                help_text="Введите почту, на которую придет ответ",
                max_length=254,
                null=True,
                verbose_name="почта",
            ),
        ),
    ]