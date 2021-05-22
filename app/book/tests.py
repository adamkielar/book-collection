from unittest.mock import Mock

from django.test import TestCase, modify_settings

@modify_settings(DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})
class DecoratorTest(TestCase):

    def test_count_query(self):
        print('hello')
