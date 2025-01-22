from django.urls import path , include

from visitor import views


app_name = "vizitor"
urlpatterns = [
    
    path('', views.index, name='index'),
    path('atividade', views.atividade, name='atividade'),
    path('konaba', views.konaba, name='konaba'),
    path('misa', views.misa, name='misa'),
    path('misa/detail/<str:id>/', views.misa_detail, name='misa_detail'),


    path('eventu', views.eventu, name='eventu'),
    path('anunsiu', views.anunsiu, name='anunsiu'),
    path('anunsiu/detail/<str:id>/', views.anunsiu_detail, name='anunsiu_detail'),

    path('atendimentu', views.atendimentu, name='atendimentu'),
    path('atendimentu_detail/<str:id>/', views.atendimentu_detail, name='atendimentu_detail'),


    path('planu', views.planu, name='planu'),
    path('detallu', views.detallu, name='detallu'),
    path('atividade/detail/<str:id>/', views.atividade_detail, name='atividade_detail'),

    path('planu/detail/<str:id>/', views.planu_detail, name='planu_detail'),


    path('perfilsazobril', views.perfilsazobril, name='perfilsazobril'),
    path('recursohumanos', views.recursohumanos, name='recursohumanos'),
    path('congregacao', views.congregacao, name='congregacao'),
    path('eskolacatolico', views.eskolacatolico, name='eskolacatolico'),
    path('grupucategorial', views.grupucategorial, name='grupucategorial'),
    path('centropastoral', views.centropastoral, name='centropastoral'),
    path('comissaun', views.comissaun, name='comissaun'),
    path('planudezenvolvimentu', views.planudezenvolvimentu, name='planudezenvolvimentu'),










                     
]


    
