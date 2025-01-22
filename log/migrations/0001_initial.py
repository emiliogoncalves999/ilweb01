# Generated by Django 5.0.6 on 2024-09-09 18:16

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
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('CREATE', 'Create'), ('UPDATE', 'Update'), ('DELETE', 'Delete')], max_length=10, verbose_name='Ação')),
                ('model_name', models.CharField(max_length=200, verbose_name='Modelo')),
                ('instance_id', models.CharField(max_length=200, verbose_name='ID Instánsia')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Data/Hora')),
                ('details', models.TextField(blank=True, null=True, verbose_name='Detalhes')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visitor_log_entries', to=settings.AUTH_USER_MODEL, verbose_name='Usuáriu')),
            ],
            options={
                'verbose_name': 'Log Entry',
                'verbose_name_plural': 'Log Entries',
            },
        ),
    ]
