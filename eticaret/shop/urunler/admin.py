from django.contrib import admin
from .models import Kategoriler, Markalar, Urunler, Etiketler, Varyasyonlar

# Kategoriler Admin Tanımı
class KategoriAdmin(admin.ModelAdmin):
    list_display = ['isim', 'seo_title', 'slug', 'aktifmi']
    list_filter = ['aktifmi', 'isim']
    search_fields = ['isim', 'seo_title', 'slug']

admin.site.register(Kategoriler, KategoriAdmin)

# Markalar Admin Tanımı
class MarkalarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'aktifmi', 'slug', 'seo_title', 'resim']
    list_filter = ['aktifmi', 'isim']
    search_fields = ['isim', 'seo_title', 'slug']

admin.site.register(Markalar, MarkalarAdmin)

# Etiketler Admin Tanımı
class EtiketlerAdmin(admin.ModelAdmin):
    list_display = ['isim']

admin.site.register(Etiketler, EtiketlerAdmin)

# Varyasyonlar Inline Tanımı
class InLineVaryasyonlar(admin.StackedInline):  # Burada iki nokta üst üste eklendi
    model = Varyasyonlar
    extra = 1

# Ürünler Admin Tanımı
class UrunlerAdmin(admin.ModelAdmin):
    list_display = ["isim", "fiyat", "marka", "kategori", "indirimlifiyat", "aktifmi", "resim", "tarih"]
    list_filter = ["aktifmi", "isim", "kategori", "marka"]
    search_fields = ["isim", "seo_title", "slug"]
    inlines = [InLineVaryasyonlar]  # 'inlines' küçük harfle yazıldı

admin.site.register(Urunler, UrunlerAdmin)
