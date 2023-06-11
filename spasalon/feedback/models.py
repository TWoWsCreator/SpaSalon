import time

from django.db import models

from users.models import CustomUser


class Feedback(models.Model):
    def get_path(self, filename):
        return f'feedback_files/{time.time()}_{filename}'
    
    user = models.ForeignKey(
        CustomUser, verbose_name="пользователь", on_delete=models.CASCADE,
        null=True, blank=True
    )
    name = models.CharField(
        'имя', max_length=150, help_text='Максимум 150 символов'
    )
    mail = models.EmailField(
        'почта', max_length=150, help_text='Максимум 150 символов'
    )
    feedback_text = models.CharField(
        'ваш отзыв', max_length=1000, help_text='Максимум 1000 символов'
    )
    created_on = models.DateTimeField(
        'дата создания', auto_now_add=True
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return self.feedback_text[:20]
