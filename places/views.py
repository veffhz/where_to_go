from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from places.models import Place
from places.serializers import place_to_json
from places.serializers import places_to_geojson


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        places = Place.objects.all()
        context['geojson'] = places_to_geojson(places)
        return context


class PlaceDetailView(View):
    def get(self, request, place_id, *args, **kwargs):
        query = Place.objects.prefetch_related('imgs')
        place = get_object_or_404(query, pk=place_id)
        data = place_to_json(place)
        return HttpResponse(data, content_type='application/json')
