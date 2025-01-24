from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from customdata.models import Author


class ActiveManager(models.Manager):
    def get_queryset(self):
        # Only return objects where is_deleted is False
        return super().get_queryset().filter(is_deleted=False)




class BaseModel(models.Model):
    user_created = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kria husi")
    is_deleted = models.BooleanField(default=False, verbose_name="Apaga",null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Data kria",null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Data muda",null=True, blank=True)

    # Custom manager to filter out deleted objects
    objects = ActiveManager()
    # Optional: Manager to include all objects (deleted and non-deleted)
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super(BaseModel, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(BaseModel, self).save(*args, **kwargs)






class Noticia(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Títulu")
    content = RichTextField(verbose_name="Konteudu")
    image = models.ImageField(upload_to='noticia_images/', blank=True, null=True, verbose_name="Imajen")
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Data publika")

    def __str__(self):
        return self.title

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Notísia"
        verbose_name_plural = "Notísias"


        

class Atividade(BaseModel):
    name = models.CharField(max_length=200, verbose_name="Titulu")
    description = RichTextField(verbose_name="Konteudu Atividade")
    image = models.ImageField(upload_to='atividade_images/', blank=True, null=True, verbose_name="Imajen")
    date = models.DateTimeField(verbose_name="Data")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Author")

    def __str__(self):
        return self.name

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"




class Eventu(BaseModel):
    name = models.CharField(max_length=200, verbose_name="Naran")
    location = models.CharField(max_length=200, verbose_name="Lokalizasaun")
    image = models.ImageField(upload_to='eventu_images/', blank=True, null=True, verbose_name="Imajen")
    date = models.DateTimeField(verbose_name="Data")

    def __str__(self):
        return self.name

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Eventu"
        verbose_name_plural = "Eventus"






class Missa(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Títulu")
    priest = models.CharField(max_length=200, verbose_name="Amo da Missa")
    date = models.DateTimeField(verbose_name="Loron",null=True,blank=True)
    time = models.TimeField(verbose_name="Oras")
    image = models.ImageField(upload_to='missa_images/', blank=True, null=True, verbose_name="Imajen")
    description = RichTextField(verbose_name="Description", null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.priest} on {self.date}"

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Missa"
        verbose_name_plural = "Missas"






class Aunsiu(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Títulu")
    message = models.TextField(verbose_name="Mensajen")
    image = models.ImageField(upload_to='aunsiu_images/', blank=True, null=True, verbose_name="Imajen")
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Data publika")

    def __str__(self):
        return self.title

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Anúnsio"
        verbose_name_plural = "Anúnsios"




class Atendimentu(BaseModel):
    name = models.CharField(max_length=200, verbose_name="Titulu")
    description = models.TextField(verbose_name="Requerementu", null=True,blank=True)
    image = models.ImageField(upload_to='atendimentu_images/', blank=True, null=True, verbose_name="Imajen")
    date = models.DateTimeField(verbose_name="Data")

    def __str__(self):
        return self.name

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Atendimentu"
        verbose_name_plural = "Atendimentos"






class AnnualPlan(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Títulu")
    description = models.TextField(verbose_name="Konteudu")
    image = models.ImageField(upload_to='atendimentu_images/', blank=True, null=True, verbose_name="Imajen")
    start_date = models.DateField(verbose_name="Data Início", null=True,blank=True)
    end_date = models.DateField(verbose_name="Data Fim", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.pk])

    class Meta:
        verbose_name = "Plano Anual"
        verbose_name_plural = "Planos Anuais"




class Attachment(models.Model):

    file = models.FileField(upload_to='attachments/')
    annual_plan = models.ForeignKey(AnnualPlan, on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)
    eventu = models.ForeignKey(Eventu, on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)
    missa = models.ForeignKey(Missa, on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)
    aunsiu = models.ForeignKey(Aunsiu, on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)
    atendimentu = models.ForeignKey(Atendimentu, on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)

    def __str__(self):
        return f"Attachment {self.file.name}"



