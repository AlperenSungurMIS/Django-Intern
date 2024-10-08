# Generated by Django 5.1.1 on 2024-09-26 08:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0006_alter_markalar_options_markalar_aciklama_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategoriler',
            name='ustkatogroi',
        ),
        migrations.AddField(
            model_name='kategoriler',
            name='ustkategori',
            field=models.ForeignKey(blank=True, help_text='Eğer bu kategori başka kategoriye bağlıysa doldurunuz', null=True, on_delete=django.db.models.deletion.CASCADE, to='urunler.kategoriler'),
        ),
        migrations.AlterField(
            model_name='markalar',
            name='isim',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='markalar',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='Urunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=155)),
                ('fiyat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('indirimlifiyat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('kisa_aciklama', models.TextField(blank=True, null=True)),
                ('aciklama', models.TextField(blank=True, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=155, null=True)),
                ('seo_description', models.TextField(blank=True, null=True)),
                ('aktifmi', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=155, null=True, unique=True)),
                ('resim', models.ImageField(blank=True, null=True, upload_to='urunresimleri/')),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urunler', to='urunler.kategoriler')),
                ('kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urunler', to='urunler.markalar')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
            },
        ),
    ]
