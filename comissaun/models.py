from django.db import models

from visitor.models import BaseModel

class Comissaun(BaseModel):
    """
    Model to represent Comissaun.
    Includes fields for name, description, logo, and contact information.
    """
    nome = models.CharField("Nome da Comissaun", max_length=255)
    deskrisaun = models.TextField("Deskrisaun")
    logo = models.ImageField(upload_to='comissaun_logos/', null=True, blank=True)  # Logo for the comissaun
    contact = models.CharField("Contact Info", max_length=255, null=True, blank=True)  # Contact information

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Comissão"
        verbose_name_plural = "Comissões"


class PlanuComisaun(BaseModel):
    """
    Model to represent PlanuComisaun (plans related to a Comissaun).
    Each plan has a title, description, file, and year.
    """
    comissaun = models.ForeignKey(Comissaun, on_delete=models.CASCADE, related_name='planus')
    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description")
    file = models.FileField(upload_to='planu_comisaun_files/', null=True, blank=True)  # Plan file
    year = models.IntegerField("Year")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Plano da Comissão"
        verbose_name_plural = "Planos da Comissão"
