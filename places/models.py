import decimal
from decimal import Decimal

from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    _short_title = models.CharField("Краткое название", max_length=200)
    short_description = models.TextField("Описание", blank=True)
    long_description = HTMLField("Полное описание", blank=True)
    lat = models.DecimalField(max_digits=16, decimal_places=14, verbose_name='Широта')
    lng = models.DecimalField(max_digits=16, decimal_places=14, verbose_name='Долгота')

    @property
    def coordinates(self):
        return {
            'lng': self.lng,
            'lat': self.lat
        }

    @property
    def short_title(self):
        return f'«{self._short_title}»'

    @property
    def round_lng(self):
        return self.lng.quantize(Decimal('1.00'), rounding=decimal.ROUND_FLOOR)

    @property
    def round_lat(self):
        return self.lat.quantize(Decimal('1.000000'), rounding=decimal.ROUND_FLOOR)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Image(models.Model):
    place_image = models.ImageField('Изображение')
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE,
        related_name='imgs', verbose_name="Место на карте"
    )
    position = models.PositiveIntegerField(
        'Позиция', default=0, blank=False, null=False
    )

    def __str__(self):
        return f"{self.position} {self.place}"

    class Meta:
        ordering = ['position']
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
