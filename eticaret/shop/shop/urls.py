from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from urunler.views import anasayfa, urundetay


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", anasayfa, name='anasayfa'),
    path("<slug:slug>/", urundetay, name='urun'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
