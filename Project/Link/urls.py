from django.urls import path
from . import views

urlpatterns = [
    path('substation-dcu/', views.substation_dcu, name='Link Substation to DCU'),
    path('substation-feeder/', views.substation_feeder, name='Link Substation to Feeder'),
    path('dcu-sim/', views.dcu_sim, name='Link DCU to Sim'),
    path('dcu-meter/', views.dcu_meter, name='Link DCU to Meter'),
    path('feeder-meter/', views.feeder_meter, name='Link Feeder to Meter'),

    ]

