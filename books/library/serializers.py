from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.response import Response

from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name')

    def create(self, validated_data):
        print('Start')
        country_data = validated_data.pop('country')
        print(country_data)
        country = Country.objects.get_or_create(**country_data)
        print(country)
        country = get_object_or_404(Country, name=country_data.get("name"))
        print(country)
        author = Author.objects.create(country_id=country.id, **validated_data)
        return author

    class Meta:
        model = Author
        fields = ['id', 'name', 'country', 'dob']


class PublishingSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name')

    def create(self, validated_data):
        country_data = validated_data.pop('country')
        Country.objects.get_or_create(**country_data)
        country = get_object_or_404(Country, name=country_data.get("name"))
        publishing = Publishing.objects.create(country_id=country.id, **validated_data)
        return publishing

    class Meta:
        model = Publishing
        fields = ['id', 'name', 'country']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')
    publishing = serializers.CharField(source='publishing.name')
    country = serializers.CharField(write_only=True)
    author_dob = serializers.DateField(write_only=True, required=False)

    def create(self, validated_data):
        print('Start')
        author_data = validated_data.pop('author')
        publishing_data = validated_data.pop('publishing')
        country_data = validated_data.pop('country')
        print(author_data)
        print(publishing_data)
        print(country_data)
        country_data = dict.fromkeys({'name'}, country_data)
        print(country_data)
        dob = ""
        if 'author_dob' in validated_data:
            dob = validated_data.pop('author_dob')
        print(dob)

        author = Author.objects.filter(name=author_data.get("name"))
        publishing = Publishing.objects.filter(name=publishing_data.get("name"))
        print(author)
        print(publishing)

        if not author:
            Country.objects.get_or_create(**country_data)
            country = get_object_or_404(Country, name=country_data.get("name"))
            print(country)
            print(author_data)
            author_data['dob'] = dob
            print(author_data)
            Author.objects.get_or_create(country_id=country.id, **author_data)

        if not publishing:
            Country.objects.get_or_create(**country_data)
            country = get_object_or_404(Country, name=country_data.get("name"))
            print(country)
            Publishing.objects.get_or_create(**publishing_data)

        author = get_object_or_404(Author, name=author_data.get("name"))
        publishing = get_object_or_404(Publishing, name=publishing_data.get("name"))
        print(author)
        print(publishing)

        book = Book.objects.create(author_id=author.id, publishing_id=publishing.id, **validated_data)
        return book

    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'instanceCount', 'dateIssue', 'author', 'publishing', 'pages', 'country',
                  'author_dob']
        extra_kwargs = {
            'country': {'write_only': True, 'source': 'country.name'},
            'author_dob': {'write_only': True, 'required': False},
            # 'security_question_answer': {'write_only': True},
            # 'password': {'write_only': True}
        }

# class BookRequestSerializer(serializers.Serializer):
#
#     def create(self, validated_data):
#
#         #split the objects into multiple objects.
#         targetDef = validated_data.pop(targetDefn)
#
#         #save the objects into its respective models.
#         targetDefId = TargetDefination.objects.create(**targetDef)
#
#         #get the objects of roleId and empID
#         role = list(validated_data['roleId'].items())
#         role_id = Role.objects.get(roleName =role[0][1])
#         emp_id = Employee.objects.get(pk=validated_data['empId']['id'])
#
#         target_obj = Target.object.create(targetDef=targetDefId, roleId=role_id, empID=emp_id, startDate=validated_data['startDate'], endDate=validated_data['endDate'], value=validated_data['value'])
#
#         return target_obj
#
#     def update(self, instance, validated_data):
#         pass
#
#     # class Meta:
#     #     model = Country
#     #     fields = ['id', 'name']
