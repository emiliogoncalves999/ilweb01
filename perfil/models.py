from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from visitor.models import BaseModel

from ckeditor.fields import RichTextField


class PerfilParoquiaSAJOBRIL(BaseModel):
    amu = models.CharField("Amu Parokia",null=True,blank=True,max_length=255)
    naran_parokia = models.CharField("Naran Parokia",null=True,blank=True,max_length=255)
    sigla_parokia = models.CharField("Sigla Parokia",null=True,blank=True,max_length=255)
    address = models.CharField("Address Parokia",null=True,blank=True,max_length=255)
    email = models.CharField("Email Parokia",null=True,blank=True,max_length=255)
    phone = models.CharField("Phone Parokia",null=True,blank=True,max_length=255)
    introdusaun = RichTextField("Introdusaun",null=True,blank=True,max_length=255)
    visao_geral = RichTextField("Visão Geral",null=True, blank=True,max_length=255)
    visao_especifica = RichTextField("Visão Específica",null=True, blank=True,max_length=255)
    missao = RichTextField("Missão", null=True, blank=True)
    istoria_existencia = RichTextField("Istoria Existencia Paróquia SAJOBRIL", null=True, blank=True)
    situacao_geral = RichTextField("Situação Geral Paróquia SJB Liquiçá", null=True, blank=True)
    area_geografica = models.ImageField(upload_to='area_geografica_images/', null=True, blank=True, verbose_name="Área Geográfica Paróquia São João de Brito Liquiçá")
    lian_nebe_usa = models.TextField("Lian nebé usa iha actividade liturgia", null=True, blank=True)
    ecp = models.ImageField(upload_to='ecp_images/', null=True, blank=True,verbose_name='Estrutura Conselho Pastoral Paróquia (CPP)')
    cep = models.ImageField(upload_to='ecp_images/', null=True, blank=True,verbose_name='Estrutura Conselho Económico Paroquial (CEP)')


    def __str__(self):
        return self.visao_geral[:50]

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Perfil Paroquial SAJOBRIL"
        verbose_name_plural = "Perfis Paroquiais SAJOBRIL"



class Congregacao(BaseModel):
    nome = models.CharField("Nome da Congregação", max_length=255)
    deskrisau = models.TextField("Deskrisau")
    imagen = models.ImageField(upload_to='congregacao/', blank=True, null=True, verbose_name="Imajen / Logo")
    file = models.FileField(upload_to='congregacoes/', null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Congregação"
        verbose_name_plural = "Congregações"

class EskolaCatolico(BaseModel):
    nome = models.CharField("Nome da Escola Católica", max_length=255)
    deskrisau = models.TextField("Deskrisau")
    imagen = models.ImageField(upload_to='eskolacatolico/', blank=True, null=True, verbose_name="Imajen / Logo")
    file = models.FileField(upload_to='eskolas/', null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Escola Católica"
        verbose_name_plural = "Escolas Católicas"

class GrupuCategorial(BaseModel):
    nome = models.CharField("Nome do Grupo Categorial", max_length=255)
    deskrisau = models.TextField("Deskrisau")
    imagen = models.ImageField(upload_to='grupucategorial/', blank=True, null=True, verbose_name="Imajen / Logo")
    file = models.FileField(upload_to='grupus/', null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Grupo Categorial"
        verbose_name_plural = "Grupos Categoriais"

class ProfessorReligiaoCatolico(BaseModel):
    nome = models.CharField("Naran Completo", max_length=255)
    fatinserviço = models.CharField("Fatin Serviço", max_length=255,blank=True, null=True)
    estatuto = models.CharField("Estatuto (Recrutado)", max_length=255,blank=True, null=True)
    kontaktu = models.CharField("Kontaktu", max_length=255, blank=True, null=True)
    descricao = models.TextField("Descrição", blank=True, null=True)
    foto = models.ImageField(upload_to='professores_religiao_catolico/', null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Professor/a Religião Católico"
        verbose_name_plural = "Professores/as Religião Católico"

class PadreMadre(BaseModel):
    GENDER_CHOICES = [
        ('padre', 'Padre Liquiçá oan'),
        ('madre', 'Madre Liquiçá oan'),
    ]
    nome = models.CharField("Naran Completo", max_length=255)
    tipo = models.CharField("Tipo", max_length=10, choices=GENDER_CHOICES)
    fatinnodataordenacao = models.DateField("Fatin no data Ordenação", blank=True, null=True)
    fatinservico = models.DateField("Fatin Serviço", blank=True, null=True)
    contacto = models.CharField("Contacto", max_length=20, blank=True, null=True)
    descricao = models.TextField("Descrição", blank=True, null=True)
    foto = models.ImageField(upload_to='padres_madres/', null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Padre/Madre"
        verbose_name_plural = "Padres/Madres"

class EisSeminaristaExReligioso(BaseModel):
    nome = models.CharField("Naran Completo", max_length=255)
    estadoeivil = models.DateField("Estado Civil", blank=True, null=True)
    contacto = models.CharField("contacto", max_length=20, blank=True, null=True)
    descricao = models.TextField("Descrição", blank=True, null=True)
    foto = models.ImageField(upload_to='eis_seminaristas_ex_religiosos/', null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Eis-Seminarista/Ex Religioso/a"
        verbose_name_plural = "Eis-Seminaristas/Ex Religiosos/as"

