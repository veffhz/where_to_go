from django.contrib import admin

from places.models import Place
from places.models import Image

admin.site.register(Place)
admin.site.register(Image)
