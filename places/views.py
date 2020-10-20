import json

from django.urls import reverse
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from places.models import Place


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        places = Place.objects.all()

        geojson = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [place.round_lng, place.round_lat]
                    },
                    'properties': {
                        "title": place.project_name,
                        "placeId": place.pk,
                        "detailsUrl": reverse('place-detail', args=(place.pk,))
                    }
                }

                for place in places
            ]
        }

        context['geojson'] = geojson

        return context


class PlaceDetailView(View):
    def get(self, request, place_id, *args, **kwargs):
        query = Place.objects.prefetch_related('imgs')
        place = get_object_or_404(query, pk=place_id)

        data = {
            "title": place.title,
            "imgs": [img.image.url for img in place.imgs.all()],
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": place.coordinates
        }

        return HttpResponse(
            json.dumps(data, default=str), content_type='application/json'
        )
