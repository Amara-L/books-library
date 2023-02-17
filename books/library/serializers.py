from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name', 'country', 'dob']


class PublishingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publishing
        fields = ['id', 'name', 'country']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'instanceCount', 'dateIssue', 'author', 'publishing', 'pages']