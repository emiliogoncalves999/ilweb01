from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Full Name")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    address = models.TextField(blank=True, null=True, verbose_name="Address")
    website = models.URLField(blank=True, null=True, verbose_name="Website")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True, verbose_name="Gender")

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
