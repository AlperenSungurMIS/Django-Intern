# Generated by Django 5.1.1 on 2024-10-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('page_number', models.IntegerField()),
                ('publish_data', models.DateField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]