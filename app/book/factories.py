import factory
from . import models


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tag
