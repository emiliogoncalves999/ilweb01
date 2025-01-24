from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from visitor.models import BaseModel



class PerfilParoquiaSAJOBRIL(BaseModel):
    amu = models.TextField("Amu Parokia",null=True,blank=True)
    naran_parokia = models.TextField("Naran Parokia",null=True,blank=True)
    sigla_parokia = models.TextField("Sigla Parokia",null=True,blank=True)
    address = models.TextField("Address Parokia",null=True,blank=True)
    email = models.TextField("Email Parokia",null=True,blank=True)
    phone = models.TextField("Phone Parokia",null=True,blank=True)
    introdusaun = models.TextField("Introdusaun",null=True,blank=True)
    visao_geral = models.TextField("Visão Geral")
    visao_especifica = models.TextField("Visão Específica")
    missao = models.TextField("Missão")
    istoria_existencia = models.TextField("Istoria Existencia Paróquia SAJOBRIL")
    situacao_geral = models.TextField("Situação Geral Paróquia SJB Liquiçá")
    area_geografica = models.ImageField(upload_to='area_geografica_images/', null=True, blank=True, verbose_name="Área Geográfica Paróquia São João de Brito Liquiçá")
    lian_nebe_usa = models.TextField("Lian nebé usa iha actividade liturgia")
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
    nome = models.CharField("Nome", max_length=255)
    data_nascimento = models.DateField("Data de Nascimento", blank=True, null=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
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
    nome = models.CharField("Nome", max_length=255)
    tipo = models.CharField("Tipo", max_length=10, choices=GENDER_CHOICES)
    data_nascimento = models.DateField("Data de Nascimento", blank=True, null=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
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
    nome = models.CharField("Nome", max_length=255)
    data_nascimento = models.DateField("Data de Nascimento", blank=True, null=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    descricao = models.TextField("Descrição", blank=True, null=True)
    foto = models.ImageField(upload_to='eis_seminaristas_ex_religiosos/', null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Eis-Seminarista/Ex Religioso/a"
        verbose_name_plural = "Eis-Seminaristas/Ex Religiosos/as"

