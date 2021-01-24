import factory
from django.contrib.auth import get_user_model

from . import models


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tag

    name = factory.Faker('word')
    owner = factory.Iterator(get_user_model().objects.all())


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Author

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Book

    title = factory.Faker('sentence', nb_words=5)
    published_date = factory.Faker('year')
    categories = factory.Faker('word', ext_word_list=['{Fiction}', '{Art}', '{History}'])
    average_rating = factory.Faker('pyfloat', left_digits=1, right_digits=2, positive=True, min_value=0, max_value=5)
    ratings_count = factory.Faker('random_number')
    owner = factory.Iterator(get_user_model().objects.all())

    author = factory.SubFactory(AuthorFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)
