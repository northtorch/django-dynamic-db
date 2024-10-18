from apps.main.models import CountData
from custom.factories import DjangoModelFactoryForMultiDatabase


class CountDataFactory(DjangoModelFactoryForMultiDatabase):
    class Meta:
        model = CountData
        django_get_or_create = ("id",)

    count = 0
