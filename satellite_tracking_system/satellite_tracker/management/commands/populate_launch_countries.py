from django.core.management.base import BaseCommand
from satellite_tracker.models import LaunchCountry

class Command(BaseCommand):
    help = 'Populate Launch Country table with dummy data'

    def handle(self, *args, **options):
        countries = ['USA', 'Russia', 'China', 'India', 'France', 'Japan', 'UK', 'Germany', 'Italy', 'Canada']
        for country in countries:
            LaunchCountry.objects.create(name=country)
        self.stdout.write(self.style.SUCCESS('Successfully populated Launch Country table.'))
