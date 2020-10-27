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
                        "title": place.short_title,
                        "placeId": place.pk,
                        "detailsUrl": reverse('place-detail', args=(place.pk,))
                    }
                }

                for place in places
            ]
        }


def place_to_json(place):
    return {
        "title": place.title,
        "imgs": [image.file.url for image in place.imgs.all()],
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": place.coordinates
    }
