from django.shortcuts import render, get_object_or_404
from .models import Kategoriler, Markalar, Urunler, Etiketler

# Anasayfa view'i
def anasayfa(request):
    urunler = Urunler.objects.filter(anasayfa=True)
    return render(request, "index.html", {"urunler": urunler})


def urundetay(request, slug):
    # Sluga göre ürünü al
    urun = get_object_or_404(Urunler, slug=slug)


    return render(request, "urun.html", {"urun": urun})
