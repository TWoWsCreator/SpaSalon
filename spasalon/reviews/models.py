from django.db import models

from users.models import CustomUser

class Rating(models.TextChoices):
    ONE = "1", "1"
    TWO = "2", "2"
    THREE = "3", "3"
    FOUR = "4", "4"
    FIVE = "5", "5"


class Reviews(models.Model):
    user = models.ForeignKey(
        CustomUser, verbose_name='пользователь', on_delete=models.CASCADE,
        null=True, blank=True
    )
    is_published = models.BooleanField(
        'публикация',
        default=True
    )
    name = models.CharField(
        'тема отзыва',
        max_length=100,
        help_text='Введите тему отзыва'
    )
    review_text = models.TextField(
        'текст отзыва',
        max_length=1000,
        help_text='Максимум 1000 символов'
    )
    rating = models.CharField(
        "оценка",
        max_length=255,
        choices=Rating.choices,
        default=Rating.THREE,
        help_text="Поставьте оценку отзыва",
    )
    created_on = models.DateField(
        'дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return self.user.username
