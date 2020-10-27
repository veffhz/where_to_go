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
    response = requests.get(url)
    response.raise_for_status()

    response = response.json()
    coordinates = response['coordinates']

    title = response['title']
    project = response['title']

    if '«' in title and '»' in title:
        part = title.split('«')[1]
        project = part.split('»')[0]
    elif '"' in title:
        project = title.split('"')[1]

    place, _ = Place.objects.get_or_create(
        title=title, defaults={
            'project': project,
            'description_short': response['description_short'],
            'description_long': response['description_long'],
            'lng': coordinates['lng'],
            'lat': coordinates['lat']
        }
    )

    links = response['imgs']

    for link_no, image_link in enumerate(links):
        response = requests.get(image_link)
        image_content_file = ContentFile(response.content)
        path, file_name = os.path.split(image_link)

        image = Image.objects.create(place=place, position=link_no)
        image.place_image.save(file_name, image_content_file, save=True)
