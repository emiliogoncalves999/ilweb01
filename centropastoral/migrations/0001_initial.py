# Generated by Django 5.0 on 2025-01-25 15:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroPastoral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Apaga')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data kria')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Data muda')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='centro_pastoral_logos/')),
                ('historia_existencia', models.TextField()),
                ('estrutura', models.ImageField(blank=True, null=True, upload_to='centro_pastoral_estrutura/', verbose_name='Estrutura Estasaun Misionario')),
                ('estruturabairo', models.ImageField(blank=True, null=True, upload_to='centro_pastoral_estrutura/', verbose_name='Estrutura Bairo sira')),
                ('estasaun_misionario', models.TextField()),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kria husi')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
