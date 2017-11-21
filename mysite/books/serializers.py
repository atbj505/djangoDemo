from rest_framework import serializers

from .models import Author, Book, Publisher


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher')

    # authors = serializers.HyperlinkedRelatedField(many=True)

    class Meta:
        model = Book
        fields = ('title', 'publisher', 'publication_date')


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('name', 'address', 'city', 'state_province', 'country', 'website')