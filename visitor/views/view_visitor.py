import os
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

from django.db.models import Count
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from datetime import date
from django.http import JsonResponse

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.utils.translation import *
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect


from django.template.loader import render_to_string

from django.contrib.auth.models import Group

from centropastoral.models import CentroPastoral
from perfil.models import Congregacao, EisSeminaristaExReligioso, EskolaCatolico, GrupuCategorial, PadreMadre, PerfilParoquiaSAJOBRIL, ProfessorReligiaoCatolico
from planodesenvolvimento.models import DettaluPlano, Planu
from visitor.models import AnnualPlan, Atendimentu, Atividade, Aunsiu, Eventu, Missa




def index(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)


    totprof = ProfessorReligiaoCatolico.objects.all().count()
    totpadre = PadreMadre.objects.filter(tipo='padre').count()
    totmadre = PadreMadre.objects.filter(tipo='madre').count()
    totseminarista = EisSeminaristaExReligioso.objects.all().count()


    atividades = Atividade.objects.all().order_by('id')

    total_atividade = Atividade.objects.all().count()
    total_planu = Planu.objects.all().count()
    total_atendimentu = Atendimentu.objects.all().count()
    total_eventu = Eventu.objects.all().count()



    paginator = Paginator(atividades, 20)  # Show 20 activities per page

    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the activities for that page




    context = {
        'total_atividade' : total_atividade,
        'perfil' : perfil,
        'total_planu' : total_planu,
        'total_atendimentu' : total_atendimentu,
        'total_eventu' : total_eventu,
        'page_obj': page_obj,
        'totprof' : totprof,
        'totpadre' : totpadre,
        'totmadre' : totmadre,
        'totseminarista' : totseminarista,

        'pajinaatividade': 'active',
    }
    return render(request,'visitor/uma.html', context)



def atividade(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)

    atividades = Atividade.objects.all().order_by('id')
    paginator = Paginator(atividades, 20)  # Show 20 activities per page

    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the activities for that page

    context = {
        'perfil' : perfil,
        'page_obj': page_obj,
        'pajinaatividade': 'active',
   # Pass the page object to the template
    }
    return render(request, 'visitor/atividade.html', context)


def atividade_detail(request, id):
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    latest_activities = Atividade.objects.exclude(id=id).order_by('-date')[:5]  # Get the latest 5 activities excluding the current one
    atividade = get_object_or_404(Atividade, pk=int(id))  # Fetch the Atividade instance by its primary key
    context = {
        'perfil' : perfil,
        'latest_activities': latest_activities,
        'atividade': atividade,  # Pass the Atividade object to the template
    }
    return render(request, 'visitor/detallu_atividade.html', context)




def konaba(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    context = {
        'perfil' : perfil,
        'pajinakonaba' : 'active',
    }
    return render(request,'visitor/konaba.html', context)



def misa(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    # Fetch and paginate Masses (Missa)
    missa_list = Missa.objects.all().order_by('id')
    missa_paginator = Paginator(missa_list, 20)  # Show 20 masses per page
    missa_page_number = request.GET.get('misa_page')  # Get the misa page number from the URL
    misa_page_obj = missa_paginator.get_page(missa_page_number)  # Get the masses for that page

    # Fetch and paginate Events (Eventu)
    event_list = Eventu.objects.all().order_by('id')
    event_paginator = Paginator(event_list, 20)  # Show 20 events per page
    event_page_number = request.GET.get('event_page')  # Get the event page number from the URL
    event_page_obj = event_paginator.get_page(event_page_number)  # Get the events for that page

    context = {
        'perfil' : perfil,
        'pajinamisa': 'active',
        'misa_page_obj': misa_page_obj,  # Pass the misa page object to the template
        'event_page_obj': event_page_obj,  # Pass the event page object to the template
    }

    return render(request, 'visitor/misa.html', context)

def misa_detail(request, id):
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    latest_misa = Missa.objects.exclude(id=id).order_by('-id')[:5]  # Get the latest 5 activities excluding the current one
    misa = get_object_or_404(Missa, pk=int(id))  # Fetch the Atividade instance by its primary key
    context = {
        'perfil' : perfil,
        'latest_misa': latest_misa,
        'misa': misa,  # Pass the Atividade object to the template
    }
    return render(request, 'visitor/detallu_misa.html', context)



    

def eventu(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    context = {
        'perfil' : perfil,
        'pajinaeventu' : 'active',
    }
    return render(request,'visitor/eventu.html', context)


def anunsiu(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    # Fetch and paginate Announcements
    announcement_list = Aunsiu.objects.all().order_by('-date_published')
    paginator = Paginator(announcement_list, 10)  # Show 10 announcements per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the announcements for that page

    context = {
        'perfil' : perfil,
        'pajinaanunsiu': 'active',
        'page_obj': page_obj,  # Pass the page object to the template
    }

    return render(request, 'visitor/anunsiu.html', context)



def anunsiu_detail(request, id):
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    latest_anunsiu = Aunsiu.objects.exclude(id=id).order_by('-id')[:5]  # Get the latest 5 activities excluding the current one
    misa = get_object_or_404(Aunsiu, pk=int(id))  # Fetch the Atividade instance by its primary key
    context = {
        'perfil' : perfil,
        'latest_misa': latest_anunsiu,
        'misa': misa,  # Pass the Atividade object to the template
    }
    return render(request, 'visitor/detallu_anunsiu.html', context)




def atendimentu(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    # Fetch and paginate Atendimentos
    atendimento_list = Atendimentu.objects.all().order_by('-date')
    paginator = Paginator(atendimento_list, 6)  # Show 6 atendimentos per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the atendimentos for that page

    context = {
        'perfil' : perfil,
        'pajinaatendimentu': 'active',
        'page_obj': page_obj,  # Pass the page object to the template
    }

    return render(request, 'visitor/atendimentu.html', context)


def atendimentu_detail(request, id):
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    atendimentu = get_object_or_404(Atendimentu, pk=int(id))
    attachments = atendimentu.attachments.all()  # Get all related attachments
    other_atendimentos = Atendimentu.objects.exclude(pk=int(id)).order_by('-date')[:5]  # Get 5 other atendimentos

    context = {
        'perfil' : perfil,
        'atendimentu': atendimentu,
        'attachments': attachments,
        'other_atendimentos': other_atendimentos,
    }

    return render(request, 'visitor/atendimentu_detail.html', context)


def planu(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    annual_plans_list = AnnualPlan.objects.all()
    paginator = Paginator(annual_plans_list, 3)  # Show 3 plans per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'perfil' : perfil,
        'pajinaplanu': 'active',
        'page_obj': page_obj,
    }
    return render(request, 'visitor/planu.html', context)



def planu_detail(request, id):
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    annual_plan = get_object_or_404(AnnualPlan, pk=int(id))
    other_plans = AnnualPlan.objects.exclude(pk=int(id))[:5]  # Fetch other plans, limiting to 5

    context = {
        'perfil' : perfil,
        'annual_plan': annual_plan,
        'other_plans': other_plans,
    }
    return render(request, 'visitor/planu_detail.html', context)



def detallu(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    context = {
        'perfil' : perfil,
        'pajinadetallu' : 'active',
    }
    return render(request,'visitor/detallu.html', context)


def perfilsazobril(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)

    perfil = PerfilParoquiaSAJOBRIL.objects.all().last()

    context = {

        'perfil' : perfil,
        'pajinadetallu' : 'active',
    }
    return render(request,'visitor/perfilsazobril.html', context)



def recursohumanos(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    profesor = ProfessorReligiaoCatolico.objects.all()
    padre = PadreMadre.objects.filter(tipo='padre')
    madre = PadreMadre.objects.filter(tipo='madre')


    exseminarista = EisSeminaristaExReligioso.objects.all()

    perfil = PerfilParoquiaSAJOBRIL.objects.all().last()

    context = {
        'perfil' : perfil,
        'profesor' : profesor,
        'padre' : padre,
        'madre' : madre,
        'exseminarista' : exseminarista,
        'pajinadetallu' : 'active',
    }
    return render(request,'visitor/recursohumanos.html', context)



def congregacao(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    congregacao = Congregacao.objects.all()
   

 
    context = {
        'perfil' : perfil,
        'congregacao' : congregacao,
      
        'pajinadetallu' : 'active',
    }
    return render(request,'visitor/congregacao.html', context)


def eskolacatolico(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    eskolacatolico = EskolaCatolico.objects.all()
   

 
    context = {
        'perfil' : perfil,
        'eskolacatolico' : eskolacatolico,
      
        'pajinadetallu' : 'active',
    }
    return render(request,'visitor/eskolacatolico.html', context)


def grupucategorial(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    grupucategorial = GrupuCategorial.objects.all()
   

 
    context = {
        'perfil' : perfil,
        'grupucategorial' : grupucategorial,
      
        'pajinadetallu' : 'active',
    }
    return render(request,'visitor/grupucategorial.html', context)

def centropastoral(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    centropastoral = CentroPastoral.objects.all()
   

 
    context = {
        'perfil' : perfil,
        'centropastoral' : centropastoral,
      
        'pajinadetallu' : 'active',
    }
    return render(request,'visitor/centropastoral.html', context)






from django.shortcuts import render
from comissaun.models import Comissaun, PlanuComisaun

def comissaun(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    # Get all Comissaun and related PlanuComisaun
    comissoes = Comissaun.objects.all()
    
    # Get a distinct list of years from PlanuComisaun
    years = PlanuComisaun.objects.values_list('year', flat=True).distinct()
    
    context = {
        'perfil' : perfil,
        'comissoes': comissoes,
        'years': years,
    }
    return render(request, 'visitor/comissaun.html', context)

def planudezenvolvimentu(request): 
    perfil = PerfilParoquiaSAJOBRIL.objects.get(id=1)
    years = DettaluPlano.objects.values_list('year', flat=True).distinct().order_by('year')
    comissoes = Planu.objects.prefetch_related('dettaluplano_set').all()

    context = {
        'perfil' : perfil,
        'years': years,
        'comissoes': comissoes,
    }

    return render(request, 'visitor/planudezenvolvimentu.html', context)
