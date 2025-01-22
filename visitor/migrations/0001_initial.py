# Generated by Django 5.0.6 on 2024-09-09 18:16

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customdata', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Apaga')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data kria')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Data muda')),
                ('title', models.CharField(max_length=200, verbose_name='Títulu')),
                ('description', models.TextField(verbose_name='Konteudu')),
                ('image', models.ImageField(blank=True, null=True, upload_to='atendimentu_images/', verbose_name='Imajen')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data Início')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Data Fim')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kria husi')),
            ],
            options={
                'verbose_name': 'Plano Anual',
                'verbose_name_plural': 'Planos Anuais',
            },
        ),
        migrations.CreateModel(
            name='Atendimentu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Apaga')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data kria')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Data muda')),
                ('name', models.CharField(max_length=200, verbose_name='Naran')),
                ('service', models.CharField(max_length=200, verbose_name='Servisu')),
                ('image', models.ImageField(blank=True, null=True, upload_to='atendimentu_images/', verbose_name='Imajen')),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kria husi')),
            ],
            options={
                'verbose_name': 'Atendimentu',
                'verbose_name_plural': 'Atendimentos',
            },
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Apaga')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data kria')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Data muda')),
                ('name', models.CharField(max_length=200, verbose_name='Titulu')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Konteudu Atividade')),
                ('image', models.ImageField(blank=True, null=True, upload_to='atividade_images/', verbose_name='Imajen')),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customdata.author', verbose_name='Author')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kria husi')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
        migrations.CreateModel(
            name='Aunsiu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Apaga')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data kria')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Data muda')),
                ('title', models.CharField(max_length=200, verbose_name='Títulu')),
                ('message', models.TextField(verbose_name='Mensajen')),
                ('image', models.ImageField(blank=True, null=True, upload_to='aunsiu_images/', verbose_name='Imajen')),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data publika')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kria husi')),
            ],
            options={
                'verbose_name': 'Anúnsio',
                'verbose_name_plural': 'Anúnsios',
            },
        ),
        migrations.CreateModel(
            name='Eventu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Apaga')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data kria')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Data muda')),
                ('name', models.CharField(max_length=200, verbose_name='Naran')),
                ('location', models.CharField(max_length=200, verbose_name='Lokalizasaun')),
                ('image', models.ImageField(blank=True, null=True, upload_to='eventu_images/', verbose_name='Imajen')),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kria husi')),
            ],
            options={
                'verbose_name': 'Eventu',
                'verbose_name_plural': 'Eventus',
            },
        ),
        migrations.CreateModel(
            name='Missa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Apaga')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data kria')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Data muda')),
                ('title', models.CharField(max_length=200, verbose_name='Títulu')),
                ('priest', models.CharField(max_length=200, verbose_name='Amo da Missa')),
                ('year', models.IntegerField(verbose_name='Tinan')),
                ('month', models.IntegerField(verbose_name='Fulan')),
                ('day', models.IntegerField(verbose_name='Loron')),
                ('time', models.TimeField(verbose_name='Tempu')),
                ('image', models.ImageField(blank=True, null=True, upload_to='missa_images/', verbose_name='Imajen')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kria husi')),
            ],
            options={
                'verbose_name': 'Missa',
                'verbose_name_plural': 'Missas',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Apaga')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data kria')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Data muda')),
                ('title', models.CharField(max_length=200, verbose_name='Títulu')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Konteudu')),
                ('image', models.ImageField(blank=True, null=True, upload_to='noticia_images/', verbose_name='Imajen')),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data publika')),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kria husi')),
            ],
            options={
                'verbose_name': 'Notísia',
                'verbose_name_plural': 'Notísias',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/')),
                ('annual_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='visitor.annualplan')),
                ('atendimentu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='visitor.atendimentu')),
                ('atividade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='visitor.atividade')),
                ('aunsiu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='visitor.aunsiu')),
                ('eventu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='visitor.eventu')),
                ('missa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='visitor.missa')),
                ('noticia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='visitor.noticia')),
            ],
        ),
    ]
