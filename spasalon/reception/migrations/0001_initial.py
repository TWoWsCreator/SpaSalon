# Generated by Django 4.2.2 on 2023-06-10 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("services", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("specialists", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reception",
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
                    "reception_date",
                    models.DateField(
                        help_text="Введите дату, на которую хотите попасть",
                        verbose_name="дата записи",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        help_text="Выберите услугу",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="service",
                        to="services.services",
                        verbose_name="услуга",
                    ),
                ),
                (
                    "specialist",
                    models.ForeignKey(
                        help_text="Введите специалиста, к которому хотите пойти",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specialist",
                        to="specialists.specialists",
                        verbose_name="специалист",
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
                "verbose_name": "запись",
                "verbose_name_plural": "записи",
            },
        ),
    ]