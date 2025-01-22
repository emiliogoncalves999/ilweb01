from django.db import models




class CentroPastoral(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='centro_pastoral_logos/')  # Path to store uploaded logos
    historia_existencia = models.TextField()
    estrutura  = models.ImageField(null=True,blank=True,upload_to='centro_pastoral_estrutura/',verbose_name='Estrutura Estasaun Misionario')
    estruturabairo   = models.ImageField(null=True,blank=True,upload_to='centro_pastoral_estrutura/',verbose_name='Estrutura Bairo sira')  # Path to store uploaded logos
    estasaun_misionario = models.TextField()

    def __str__(self):
        return f'Perfil of {self.name}'