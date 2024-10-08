from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Kategoriler(models.Model):
    isim = models.CharField(max_length=155)
    ustkategori = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                    help_text="Eğer bu kategori başka kategoriye bağlıysa doldurunuz")
    aktifmi = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Kategoriler"
        verbose_name = "Kategori"

    def __str__(self):
        return self.isim


class Markalar(models.Model):
    isim = models.CharField(max_length=255, default="")
    resim = models.ImageField(upload_to='markaresimleri/', blank=True, null=True)
    aciklama = models.TextField(blank=True, null=True)
    seo_title = models.CharField(max_length=255, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=255, default="")
    aktifmi = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Markalar"
        verbose_name = "Marka"

    def __str__(self):
        return self.isim


class Etiketler(models.Model):
    isim = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.isim


class Urunler(models.Model):
    isim = models.CharField(max_length=155)
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    indirimlifiyat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    kisa_aciklama = models.TextField(blank=True, null=True)
    aciklama = models.TextField(blank=True, null=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    aktifmi = models.BooleanField(default=True)
    slug = models.SlugField(max_length=155, unique=True, null=True, blank=True)
    resim = models.ImageField(upload_to='urunresimleri/', blank=True, null=True)
    tarih = models.DateTimeField(auto_now_add=True)
    marka = models.ForeignKey(Markalar, on_delete=models.CASCADE)
    kategori = models.ForeignKey(Kategoriler, on_delete=models.CASCADE)
    etiketler = models.ManyToManyField(Etiketler, blank=True)
    anasayfa = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Ürünler"
        verbose_name = "Ürün"

    def __str__(self):
        return self.isim

    def save(self, *args, **kwargs):
        # Eğer slug boşsa, isime göre otomatik oluştur.
        if not self.slug:
            self.slug = slugify(self.isim)

        # Eğer indirimli fiyat girilmemişse, normal fiyatı kullan.
        if not self.indirimlifiyat:
            self.indirimlifiyat = self.fiyat

        # Standart save fonksiyonunu çağır.
        super(Urunler, self).save(*args, **kwargs)


class Varyasyonlar(models.Model):
    urun = models.ForeignKey(Urunler, on_delete=models.CASCADE)
    varyasyon = models.CharField(max_length=155)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()
    aktifmi = models.BooleanField(default=True)
    resim = models.ImageField(upload_to="varyasyonresimleri", blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Varyasyonlar"
        verbose_name = "Varyasyon"

    def __str__(self):
        return self.varyasyon
