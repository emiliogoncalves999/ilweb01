# Generated by Django 5.0.6 on 2024-10-31 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missa',
            name='day',
        ),
        migrations.RemoveField(
            model_name='missa',
            name='month',
        ),
        migrations.RemoveField(
            model_name='missa',
            name='year',
        ),
        migrations.AddField(
            model_name='missa',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Loron'),
        ),
        migrations.AlterField(
            model_name='missa',
            name='time',
            field=models.TimeField(verbose_name='Oras'),
        ),
    ]
