from operator import truediv

from django.db import models

class Kategoriler(models.Model):
    isim=models.CharField(max_length=155)
    ustkatogroi=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,
    help_text="Eğer bu kategori başka katogeriye bağlıysa doldurunuz" )
    aktifmi=models.BooleanField(default=True)
    seo_title=models.CharField(max_length=155,blank=True,null=True)
    seo_description=models.TextField(blank=True,null=True)
    class Meta:
        verbose_name_plural="Kategoriler"
        verbose_name="Kategori"
    def __str__(self):
        return self.isim