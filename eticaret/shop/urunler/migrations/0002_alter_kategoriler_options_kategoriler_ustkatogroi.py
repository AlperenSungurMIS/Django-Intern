# Generated by Django 5.1.1 on 2024-09-24 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategoriler',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AddField(
            model_name='kategoriler',
            name='ustkatogroi',
            field=models.ForeignKey(blank=True, help_text='Eğer bu kategori başka katogeriye bağlıysa doldurunuz', null=True, on_delete=django.db.models.deletion.CASCADE, to='urunler.kategoriler'),
        ),
    ]