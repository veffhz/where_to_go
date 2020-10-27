import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Master data import'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL for json file download')

    def handle(self, *args, **options):
        run(options['url'])


def run(url):
    response = requests.get(url, allow_redirects=False)
    response.raise_for_status()

    response = response.json()
    coordinates = response['coordinates']

    title = response['title']
    short_title = response['title']

    if '«' in title and '»' in title:
        part = title.split('«')[1]
        short_title = part.split('»')[0]
    elif '"' in title:
        short_title = title.split('"')[1]

    place, _ = Place.objects.get_or_create(
        title=title, defaults={
            '_short_title': short_title,
            'short_description': response['short_description'],
            'long_description': response['long_description'],
            'lng': coordinates['lng'],
            'lat': coordinates['lat']
        }
    )

    links = response['imgs']

    for link_no, image_link in enumerate(links):
        response = requests.get(image_link, allow_redirects=False)
        response.raise_for_status()

        image_content_file = ContentFile(response.content)
        path, file_name = os.path.split(image_link)

        image = Image.objects.create(place=place, position=link_no)
        image.file.save(file_name, image_content_file, save=True)
