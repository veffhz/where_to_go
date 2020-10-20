from django.db import models


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description_short = models.CharField("Описание", max_length=5000)
    description_long = models.TextField("Полное описание")
    lat = models.DecimalField('Latitude', max_digits=16, decimal_places=14)
    lng = models.DecimalField('Longitude', max_digits=16, decimal_places=14)

    def coordinates(self):
        return {
            "lng": self.lng,
            "lat": self.lat
        }

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Изображение')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='imgs',)

    def __str__(self):
        return f"{self.pk} {self.place}"

    class Meta:
        ordering = ['-id']
