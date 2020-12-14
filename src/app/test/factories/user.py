import factory
from django.contrib.auth import get_user_model
from pytest_factoryboy import register


@register
class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = get_user_model()
