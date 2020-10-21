import json

from django.urls import reverse


def places_to_geojson(places):
    return {
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


def place_to_json(place):
    data = {
        "title": place.title,
        "imgs": [img.image.url for img in place.imgs.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": place.coordinates
    }

    return json.dumps(data, default=str)
