from apps.master.models import MasterCountData
from custom.factories import DjangoModelFactoryForMultiDatabase


class MasterCountDataDataFactory(DjangoModelFactoryForMultiDatabase):
    class Meta:
        model = MasterCountData
        django_get_or_create = ("id",)

    count = 0
