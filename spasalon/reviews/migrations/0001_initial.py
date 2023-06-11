# Generated by Django 4.2.2 on 2023-06-10 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Reviews",
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
                ("is_published", models.BooleanField(verbose_name="публикация")),
                (
                    "name",
                    models.CharField(
                        help_text="Введите тему отзыва",
                        max_length=100,
                        verbose_name="тема отзыва",
                    ),
                ),
                ("review_text", models.TextField(verbose_name="текст отзыва")),
                (
                    "type_of_court",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                        ],
                        default="3",
                        help_text="Поставьте оценка отзыва",
                        max_length=255,
                        verbose_name="оценка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "отзыв",
                "verbose_name_plural": "отзывы",
            },
        ),
    ]
