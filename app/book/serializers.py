from rest_framework import serializers
from .models import Author, Book, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name'
        )
        read_only_fields = ('id',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
        )
        read_only_fields = ('id',)


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault)
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'owner',
            'title',
            'published_date',
            'categories',
            'average_rating',
            'ratings_count',
            'author',
            'tags',
        )
        read_only_fields = ('id', 'owner')
