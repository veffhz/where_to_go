import decimal
from decimal import Decimal

from django.db import models


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    project = models.CharField("Проект", max_length=200, null=True)
    description_short = models.CharField("Описание", max_length=5000)
    description_long = models.TextField("Полное описание")
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

    def __str__(self):
        return f"{self.pk} {self.place}"

    class Meta:
        ordering = ['-id']
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
