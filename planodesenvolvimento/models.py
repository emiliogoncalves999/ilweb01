from django.db import models

from django.db import models

class Planu(models.Model):
    """
    Model to represent Comissaun.
    Includes fields for name, description, logo, and contact information.
    """
    nome = models.CharField("Planu dezenvolvimentu ba  ?", max_length=255)
    deskrisaun = models.TextField("Deskrisaun")
    contact = models.CharField("Contact Info", max_length=255, null=True, blank=True)  # Contact information

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Palnu Dezenvolvimentu"
        verbose_name_plural = "Palnu Dezenvolvimentu"


class DettaluPlano(models.Model):
    """
    Model to represent PlanuComisaun (plans related to a Comissaun).
    Each plan has a title, description, file, year, and a relation to Planu.
    """
    planu = models.ForeignKey(Planu, related_name='dettaluplano_set', on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description")
    file = models.FileField(upload_to='planu_comisaun_files/', null=True, blank=True)  # Plan file
    year = models.IntegerField("Year")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Planu dezenvolvimentu Detallu"
        verbose_name_plural = "Planu dezenvolvimentu Detallu"
