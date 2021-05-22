from django.db.models import Prefetch
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Author, Book, Tag
from .serializers import BookSerializer
from .decorators import count_query


class BookViewSet(viewsets.ModelViewSet):
    allowed_methods = ['GET']
    queryset = Book.objects.all()
    #queryset = Book.objects.order_by('tags__name')
    #queryset = Book.objects.select_related('author')
    # queryset = Book.objects.select_related('author').prefetch_related('tags')
    # queryset = Book.objects.prefetch_related(
    #      Prefetch('tags', queryset=Tag.objects.order_by('name'))
    #  ).order_by('tags__name')
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['published_date']

    @count_query
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BookView(viewsets.ViewSet):

    @count_query
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
