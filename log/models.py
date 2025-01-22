from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LogEntry(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]

    action = models.CharField(max_length=10, choices=ACTION_CHOICES, verbose_name="Ação")
    model_name = models.CharField(max_length=200, verbose_name="Modelo")
    instance_id = models.CharField(max_length=200, verbose_name="ID Instánsia")  # Changed to CharField
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Usuáriu", related_name='visitor_log_entries')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Data/Hora")
    details = models.TextField(blank=True, null=True, verbose_name="Detalhes")

    def __str__(self):
        return f"{self.action} - {self.model_name} - ID {self.instance_id} - {self.timestamp}"

    class Meta:
        verbose_name = "Log Entry"
        verbose_name_plural = "Log Entries"