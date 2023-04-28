from django.urls import path
from . import views

urlpatterns = [
    path('substation/', views.substation, name='delete substation '),
    path('dcu/', views.dcu, name='delete dcu '),
    path('feeder/', views.feeder, name='delete feeder '),
    path('sim/', views.sim, name='delete sim '),
    path('meter/', views.meter, name='delete meter '),
    path('virtualgroup/', views.virtual_group, name='delete virtual_group '),
    path('substation-dcu/', views.substation_dcu, name='delete link-substation-dcu '),
    path('substation-feeder/', views.substation_feeder, name='delete link-substation-feeder '),
    path('dcu-sim/', views.dcu_sim, name='delete link-dcu-sim '),
    path('dcu-meter/', views.dcu_meter_config, name='delete link-dcu-meter '),
    path('feeder-meter/', views.feeder_meter, name='delete link-feeder-meter '),
    path('virtualgroup-meter/', views.virtual_group_meter, name='delete link-virtual_group-meter columns')

    ]

