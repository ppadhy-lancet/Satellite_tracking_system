# File: populate_satellites.py
import requests
from django.core.management.base import BaseCommand
from satellite_tracker.models import Satellite

class Command(BaseCommand):
    help = 'Populate Satellites table with data from JSON API'

    def handle(self, *args, **options):
        url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"
        response = requests.get(url)
        
        if response.status_code == 200:
            json_data = response.json()
            satellites_data = json_data

            satellites_to_create = []
            for satellite_data in satellites_data:
                satellite = Satellite(
                    object_name=satellite_data['OBJECT_NAME'],
                    object_id=satellite_data['OBJECT_ID'],
                    epoch=satellite_data['EPOCH'],
                    mean_motion=satellite_data['MEAN_MOTION'],
                    eccentricity=satellite_data['ECCENTRICITY'],
                    inclination=satellite_data['INCLINATION'],
                    ra_of_asc_node=satellite_data['RA_OF_ASC_NODE'],
                    arg_of_pericenter=satellite_data['ARG_OF_PERICENTER'],
                    mean_anomaly=satellite_data['MEAN_ANOMALY'],
                    ephemeris_type=satellite_data['EPHEMERIS_TYPE'],
                    classification_type=satellite_data['CLASSIFICATION_TYPE'],
                    norad_cat_id=satellite_data['NORAD_CAT_ID'],
                    element_set_no=satellite_data['ELEMENT_SET_NO'],
                    rev_at_epoch=satellite_data['REV_AT_EPOCH'],
                    bstar=satellite_data['BSTAR'],
                    mean_motion_dot=satellite_data['MEAN_MOTION_DOT'],
                    mean_motion_ddot=satellite_data['MEAN_MOTION_DDOT']
                )
                satellites_to_create.append(satellite)

            Satellite.objects.bulk_create(satellites_to_create)
            self.stdout.write(self.style.SUCCESS('Satellites table populated successfully.'))
        else:
            self.stderr.write(self.style.ERROR('Failed to fetch data from JSON API. Status code: {}'.format(response.status_code)))
