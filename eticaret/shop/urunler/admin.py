from django.contrib import admin
from django.contrib.admin import ModelAdmin
from.models import Kategoriler
from .models import Kategoriler,Markalar

# Register your models here.

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['isim', 'seo_title', 'slug', 'aktifmi']
    list_filter = ['aktifmi','isim']
    search_fields = ['isim', 'seo_title', 'slug']


admin.site.register(Kategoriler,KategoriAdmin)
class MarkalarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'aktifmi','slug','seo_title','resim']
    list_filter = ['aktifmi', 'isim']
    search_fields = ['isim', 'seo_title',  'slug']

admin.site.register(Markalar,MarkalarAdmin)