from rest_framework import serializers
from books.models import Book


""" **************** This Class allows you to specify the serializers for Books ****************  """

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('created_date',)


""" **************** This Class allows you to specify the serializers for External Books ****************  """

class ExternalBookSerializer(serializers.Serializer):
    name = serializers.CharField()
    isbn = serializers.CharField()
    authors = serializers.ListField(child=serializers.CharField())
    number_of_pages = serializers.IntegerField(source='numberOfPages')
    publisher = serializers.CharField()
    country = serializers.CharField()
    release_date = serializers.DateField(source='released')