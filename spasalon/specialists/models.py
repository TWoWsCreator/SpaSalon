from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

class Specialists(models.Model):
    name = models.CharField(
        'имя',
        max_length=50
    )
    surname = models.CharField(
        'фамилия',
        max_length=50
    )
    description = models.TextField(
        'о специалисте'
    )
    person_image = models.ImageField(
        'путь до изображения специалиста',
        upload_to='items/',
    )
    is_published = models.BooleanField(
        'опубликовано',
        default=True
    )

    @property
    def get_image(self):
        return get_thumbnail(self.person_image, '250x250', quality=51)

    def image_tmb(self):
        if self.person_image:
            return mark_safe(f'<img src={self.get_image.url} />')
        return 'нет изображения'

    image_tmb.short_description = 'изображение товара'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'специалист'
        verbose_name_plural = 'специалисты'

    def __str__(self):
        return self.name
