from django.urls import path
from . import views

urlpatterns = [
    path('substation/', views.substation, name='Register Substation Master'),
    path('dcu/', views.dcu_master, name='Register DCU Master'),
    path('feeder/', views.feeder_master, name='Register Feeder Master'),
    path('sim/', views.sim_master, name='Register Sim Master'),
    path('meter/', views.meter_master, name='Register Meter Master'),
    path('virtualgroup/', views.virtual_group_master, name='Register Virtual Group Master and linked to meter id'),

    ]


