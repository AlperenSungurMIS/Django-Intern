from operator import truediv
from symtable import Class
from django.contrib.auth.models import User
from django.db import models

class Kategoriler(models.Model):
    isim=models.CharField(max_length=155)
    ustkatogroi=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,
    help_text="Eğer bu kategori başka katogeriye bağlıysa doldurunuz" )
    aktifmi=models.BooleanField(default=True)
    seo_title=models.CharField(max_length=155,blank=True,null=True)
    seo_description=models.TextField(blank=True,null=True)
    slug=models.SlugField(max_length=155,unique=True,null=True,blank=True)
    class Meta:
        verbose_name_plural="Kategoriler"
        verbose_name="Kategori"
    def __str__(self):
        return self.isim
class Markalar(models.Model):
        isim = models.CharField(max_length=255, default="")  # Marka ismi
        resim = models.ImageField(upload_to='markaresimleri/', blank=True,
                                 null=True)  # Marka logosu için dosya yükleme alanı
        aciklama =models.TextField(blank=True,null=True)
        seo_title = models.CharField(max_length=255, blank=True, null=True)  # SEO başlığı
        seo_description = models.TextField(blank=True, null=True)  # SEO açıklaması
        slug = models.SlugField(unique=True, max_length=255, default="")  # URL için benzersiz slug
        aktifmi = models.BooleanField(default=True)  # Markanın aktif olup olmadığını belirleyen alan
        class Meta:
            verbose_name_plural="Markalar"
            verbose_name="Marka"
        def __str__(self):
            return self.isim

class Urunler(models.Model):
        isim = models.CharField(max_length=155)
        kullanici=models.ForeignKey(User, on_delete=models.CASCADE)
        fiyat=models.DecimalField(max_digits=10,decimal_places=2)
        indirimlifiyat=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
        kisa_aciklama=models.TextField(blank=True,null=True)
        aciklama=models.TextField(blank=True,null=True)
        seo_title=models.CharField(max_length=155,blank=True,null=True)
        seo_description=models.TextField(blank=True,null=True)
        aktifmi=models.BooleanField(default=True)
        slug=models.SlugField(max_length=155,unique=True,null=True,blank=True)
        resim = models.ImageField(upload_to='urunresimleri/', blank=True, null=True)
        tarih = models.DateTimeField(auto_now_add=True)