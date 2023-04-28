from django.urls import path, include
from . import views

urlpatterns = [

    path('monitor/', views.joins, name='joined'),
    path('monitor_meter/', views.DataAnalysis.as_view(), name='monitor_meter'),
    path('ins_monitor/', views.InstantData.as_view(), name='ins_monitor'),
    path('retrieve/<str:table_code>/<str:date_from>/<str:date_to>/<str:meter>/<str:col_code>/', views.Retrieve, name='retrieve'),
    path('meterId_ser_num/', views.Meter_Retrieve.as_view(),name='meterId_ser_num'),
    path('description/<str:table_code>/', views.description,name='description'),
    path('table_des/', views.Table_desc.as_view(), name='table_des'),
    path('ins/', views.Ins.as_view(), name='ins'),
    path('block/', views.Block.as_view(), name='block'),
    path('daily/', views.Daily.as_view(), name='daily'),
]
