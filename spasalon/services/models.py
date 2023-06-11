from django.db import models
from django.utils.safestring import mark_safe

from sorl.thumbnail import get_thumbnail

class Services(models.Model):
    name = models.CharField(
        'название услуги',
        max_length=50
    )
    is_published = models.BooleanField(
        'публикация',
        default=True
    )
    description = models.TextField(
        'описание услуги'
    )
    price = models.IntegerField(
        'стоимость услуги'
    )
    main_image = models.ImageField(
        'путь до изображения товара',
        upload_to='items/',
        null=True,
        blank=True
    )

    @property
    def get_image(self):
        return get_thumbnail(self.main_image, '250x150', quality=51)

    def image_tmb(self):
        if self.main_image:
            return mark_safe(f'<img src={self.get_image.url} />')
        return 'нет изображения'

    image_tmb.short_description = 'изображение товара'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    def __str__(self):
        return self.name
    

class ServiceImages(models.Model):
    service_photos = models.ForeignKey(
        Services,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='фотографии товара',
    )
    image = models.ImageField(
        'путь до фотографии товара',
        upload_to='items/',
    )

    @property
    def get_image(self):
        return get_thumbnail(self.image, '600x300', crop='center', quality=51)

    def image_tmb(self):
        if self.gallery_image:
            return mark_safe(f'<img src={self.get_image.url} /')
        return 'нет изображения'

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'фотография изображения'
        verbose_name_plural = 'фотографии изображения'