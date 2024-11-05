from django.core.serializers import serialize
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from book_api.models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from book_api.serializer import BookSerializer
from rest_framework import status

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book(request, id):
    try:
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({"error": "Eşleşen kayıt bulunamadı"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["PUT"])
def book_update(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response({"error": "Eşleşen kayıt bulunamadı"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def book_delete(request, id):
    try:
        book = Book.objects.get(pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response({"error": "Eşleşen kayıt bulunamadı"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
