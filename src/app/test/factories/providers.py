from django.contrib.gis.geos.point import Point
from faker import Faker
from faker.providers.python import BaseProvider

fake = Faker()


class DjangoGeoPointProvider(BaseProvider):

    def geo_point(self, **kwargs):
        kwargs['coords_only'] = True
        coords = fake.local_latlng(**kwargs)
        return Point(x=float(coords[1]), y=float(coords[0]), srid=4326)
