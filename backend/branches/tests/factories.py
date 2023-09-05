import factory
from app.test.factories import DjangoGeoPointProvider
from branches.models import Branch


class BranchFactory(factory.django.DjangoModelFactory):
    factory.Faker.add_provider(DjangoGeoPointProvider)

    name = factory.Faker('company')
    location = factory.Faker('geo_point', country_code='US')

    class Meta:
        model = Branch
        django_get_or_create = ('name', )
