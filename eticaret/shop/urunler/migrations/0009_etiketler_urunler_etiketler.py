# Generated by Django 5.1.1 on 2024-09-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0008_alter_urunler_kategori_alter_urunler_marka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiketler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='urunler',
            name='etiketler',
            field=models.ManyToManyField(blank=True, to='urunler.etiketler'),
        ),
    ]