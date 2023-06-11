from django.db import models

from services.models import Services
from specialists.models import Specialists
from users.models import CustomUser

class Reception(models.Model):
    user = models.ForeignKey(
        CustomUser, verbose_name='пользователь', on_delete=models.CASCADE,
        null=True, blank=True
    )
    mail = models.EmailField(
        'почта',
        help_text='Введите почту, на которую придет ответ',
        null=True, blank=True
    )
    service = models.ForeignKey(
        Services,
        related_name='service',
        verbose_name='услуга',
        on_delete=models.CASCADE,
        help_text='Выберите услугу'
    )
    specialist = models.ForeignKey(
        Specialists,
        related_name='specialist',
        verbose_name='специалист',
        on_delete=models.CASCADE,
        help_text='Введите специалиста, к которому хотите пойти'
    )
    reception_date = models.DateField(
        'дата записи',
        help_text='Введите дату, на которую хотите попасть'
    )

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

    def __str__(self):
        return self.user.username