import factory
from django.db.utils import ConnectionRouter

router = ConnectionRouter()


class DjangoModelFactoryForMultiDatabase(factory.django.DjangoModelFactory):

    @classmethod
    def _get_manager(cls, model_class):
        if model_class is None:
            raise factory.errors.AssociatedClassError(f"No model set on {cls.__module__}.{cls.__name__}.Meta")

        try:
            manager = model_class.objects
        except AttributeError:
            # When inheriting from an abstract model with a custom
            # manager, the class has no 'objects' field.
            manager = model_class._default_manager

        db = router.db_for_write(model_class, instance=None)
        manager = manager.using(db)
        return manager
