import decimal
from decimal import Decimal

from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    project = models.CharField("Проект", max_length=200, null=True)
    description_short = models.TextField("Описание")
    description_long = HTMLField("Полное описание")
    lat = models.DecimalField('Latitude', max_digits=16, decimal_places=14)
    lng = models.DecimalField('Longitude', max_digits=16, decimal_places=14)

    @property
    def coordinates(self):
        return {
            'lng': self.lng,
            'lat': self.lat
        }

    @property
    def project_name(self):
        return f'«{self.project}»'

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
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='imgs',)
    position = models.PositiveIntegerField('Позиция', default=0, blank=False, null=False)

    def __str__(self):
        return f"{self.position} {self.place}"

    class Meta:
        ordering = ['position']
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
