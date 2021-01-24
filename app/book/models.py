from django.db import models
from django.conf import settings

from django.contrib.postgres.fields import ArrayField


class Owner(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Tag(Owner):
    name = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='book_tag_name_index')
        ]

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['last_name'], name='book_author_last_name_index'),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(Owner):
    title = models.TextField()
    published_date = models.CharField(max_length=10, blank=True)
    categories = ArrayField(
        models.CharField(max_length=255, null=True, blank=True),
        size=5,
        null=True,
        blank=True,
        default=list
    )
    average_rating = models.PositiveSmallIntegerField(blank=True, default=0)
    ratings_count = models.PositiveIntegerField(blank=True, default=0)
    thumbnail = models.TextField(blank=True, null=True)

    author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    class Meta:
        indexes = [
            models.Index(fields=['title'], name='book_book_title_index'),
        ]

    def __str__(self):
        return self.title
