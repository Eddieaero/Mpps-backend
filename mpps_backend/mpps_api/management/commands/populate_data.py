import json
from django.core.management.base import BaseCommand
from mpps_api.models import Destination, Point

class Command(BaseCommand):
    help = 'Populates the database with location data'

    def handle(self, *args, **kwargs):
        with open('MPPS-Backend/mpps_backend/mpps_api/points.json', 'r') as file:
            data = json.load(file)

            for entry in data[0]['destination']:
                Destination.objects.create(
                    name=entry['name'],
                    region=entry['region'],
                    latitude=entry['coordinates']['lat'],
                    longitude=entry['coordinates']['lng']
                )

            for entry in data[1]['points']:
                Point.objects.create(
                    name=entry['name'],
                    code=entry['code'],
                    lng=entry['lng'],
                    lat=entry['lat']
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
