from django.shortcuts import render
from .models import Etiketler,Urunler,Kategoriler,Markalar

# Create your views here.

def anasayfa(request):
    urunler=Urunler.objects.all()
    return render(request, "index.html",{"urunler":urunler})

