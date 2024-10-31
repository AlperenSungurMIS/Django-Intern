from book_api.models import Book
from django.http import JsonResponse
from django.shortcuts import render

def book_list(request):
    books = Book.objects.all()
    books_list = list(books.values())
    return JsonResponse({
        "books": books_list
    })

def create(request):
    pass
