from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .serializers import *
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from django.http.response import JsonResponse


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def country_view(request):
    if request.method == 'GET':
        country_id = request.query_params.get('country_id')
        if country_id is not None:
            country = get_object_or_404(Country, id=country_id)
            country_serializer = CountrySerializer(country)
            return JsonResponse(country_serializer.data, safe=False)
        else:
            countries = Country.objects.all()
            country_serializer = CountrySerializer(countries, many=True)
            return JsonResponse(country_serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country_id = request.query_params.get('country_id')
        if country_id is None or not country_id.isdigit():
            return Response("Field country_id is required", status=status.HTTP_400_BAD_REQUEST)

        country = get_object_or_404(Country, id=country_id)
        country.delete()
        return Response('Ok', 200)

@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def author_view(request):
    if request.method == 'GET':
        author_id = request.query_params.get('author_id')
        if author_id is not None:
            author = get_object_or_404(Author, id=author_id)
            author_serializer = AuthorSerializer(author)
            return JsonResponse(author_serializer.data, safe=False)
        else:
            authors = Author.objects.all()
            author_serializer = AuthorSerializer(authors, many=True)
            return JsonResponse(author_serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        author_id = request.query_params.get('author_id')
        if author_id is None or not author_id.isdigit():
            return Response("Field author_id is required", status=status.HTTP_400_BAD_REQUEST)

        author = get_object_or_404(Author, id=author_id)
        author.delete()
        return Response('Ok', 200)


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def publishing_view(request):
    if request.method == 'GET':
        publishing_id = request.query_params.get('publishing_id')
        if publishing_id is not None:
            publishing = get_object_or_404(Publishing, id=publishing_id)
            publishing_serializer = PublishingSerializer(publishing)
            return JsonResponse(publishing_serializer.data, safe=False)
        else:
            countries = Publishing.objects.all()
            publishing_serializer = PublishingSerializer(countries, many=True)
            return JsonResponse(publishing_serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = PublishingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        publishing_id = request.query_params.get('publishing_id')
        if publishing_id is None or not publishing_id.isdigit():
            return Response("Field publishing_id is required", status=status.HTTP_400_BAD_REQUEST)

        publishing = get_object_or_404(Publishing, id=publishing_id)
        publishing.delete()
        return Response('Ok', 200)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def book_view(request):
    if request.method == 'GET':
        book_id = request.query_params.get('book_id')
        if book_id is not None:
            book = get_object_or_404(Book, id=book_id)
            book_serializer = BookSerializer(book)
            return JsonResponse(book_serializer.data, safe=False)
        else:
            countries = Book.objects.all()
            book_serializer = BookSerializer(countries, many=True)
            return JsonResponse(book_serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book_id = request.query_params.get('book_id')
        if book_id is None or not book_id.isdigit():
            return Response("Field book_id is required", status=status.HTTP_400_BAD_REQUEST)

        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return Response('Ok', 200)

    elif request.method == 'PUT':

        books = Book.objects.filter(author=2)
        book_serializer = BookSerializer(books, many=True)
        return JsonResponse(book_serializer.data, safe=False)
        #
        # serializer = BookSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.data.get()
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


