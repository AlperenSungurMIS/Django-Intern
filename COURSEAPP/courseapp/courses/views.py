from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

def kurslar(request):
    return HttpResponse('Kurs listesi')

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} detay sayfası')

def getCoursesByCategory(request, category_name):
    text = ""
    if category_name == "programlama":
        text = "Programlama kategorisine ait kurslar"
    elif category_name == "web-gelistirme":
        text = "Web geliştirme kategorisine ait kurslar"
    else:
        text = "Yanlış kategori seçimi"
    return HttpResponse(text)

def getCoursesByCategoryId(request, category_id):
    # Örnek olarak kategori ID'si "1" olanlar programlama kurslarına yönlendiriliyor
    if category_id == "1":
        return HttpResponseRedirect('/programlama')
    else:
        return HttpResponse('Yanlış kategori ID')
