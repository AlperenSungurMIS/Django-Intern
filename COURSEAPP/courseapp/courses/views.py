from django.shortcuts import render
from django.http import HttpResponse

def kurslar(request):
    return HttpResponse('kurs listesi')
def programlama(request):
    return HttpResponse('programlama kurs listesi')
def mobiluygulamalar(request):
    return HttpResponse('mobil uygulanamalar programlama kurs listesi')
def details(request):
    return HttpResponse('kurs detay sayfası')
def getCoursesByCategory(request, category):
    text = " "
    if(category == "programlama"):
        text = "programlama kategorisine ait kurslar"
    elif(category == "web-gelistirme"):
        text = "yanlış kategori seçimi"
    else :
        text = "yanlış kategori seçimi"
    return HttpResponse(text)


