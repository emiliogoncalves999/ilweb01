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
            name='Planu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Apaga')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data kria')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Data muda')),
                ('nome', models.CharField(max_length=255, verbose_name='Planu dezenvolvimentu ba  ?')),
                ('deskrisaun', models.TextField(verbose_name='Deskrisaun')),
                ('contact', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contact Info')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kria husi')),
            ],
            options={
                'verbose_name': 'Planu Dezenvolvimentu',
                'verbose_name_plural': 'Planu Dezenvolvimentu',
            },
        ),
        migrations.CreateModel(
            name='DettaluPlano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Apaga')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data kria')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Data muda')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('file', models.FileField(blank=True, null=True, upload_to='planu_comisaun_files/')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kria husi')),
                ('planu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dettaluplano_set', to='planodesenvolvimento.planu')),
            ],
            options={
                'verbose_name': 'Planu dezenvolvimentu Detallu',
                'verbose_name_plural': 'Planu dezenvolvimentu Detallu',
            },
        ),
    ]
