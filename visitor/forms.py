# dashboard/forms.py
from django import forms
from .models import Noticia, Atividade, Eventu, Missa, Aunsiu, Atendimentu, Attachment

class AttachmentInlineForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file']

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'date_published': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class EventuForm(forms.ModelForm):
    class Meta:
        model = Eventu
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class MissaForm(forms.ModelForm):
    class Meta:
        model = Missa
        fields = '__all__'
        widgets = {
            'year': forms.NumberInput(attrs={'min': 1900}),
            'month': forms.NumberInput(attrs={'min': 1, 'max': 12}),
            'day': forms.NumberInput(attrs={'min': 1, 'max': 31}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class AunsiuForm(forms.ModelForm):
    class Meta:
        model = Aunsiu
        fields = '__all__'
        widgets = {
            'date_published': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AtendimentuForm(forms.ModelForm):
    class Meta:
        model = Atendimentu
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
