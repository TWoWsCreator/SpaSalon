from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(
        "имя пользователя",
        max_length=30,
        unique=True,
        help_text="Максимальная длина 30 символов",
    )
    email = models.EmailField(
        "ваша почта",
        unique=True,
    )

    def __str__(self):
        return self.username


class PasswordResetEmail(models.Model):
    user_email = models.EmailField(
        "ваша почта",
    )

    def __str__(self):
        return self.user_email
