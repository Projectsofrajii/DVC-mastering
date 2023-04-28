from django.urls import path
from . import views

urlpatterns = [
    path('substation/', views.substation, name='update substation columns'),
    path('dcu/', views.dcu, name='update dcu columns'),
    path('feeder/', views.feeder, name='update feeder columns'),
    path('sim/', views.sim, name='update sim columns'),
    path('meter/', views.meter, name='update meter columns'),
    path('virtualgroup/', views.virtual_group, name='update virtual_group columns'),
    path('substation-dcu/', views.substation_dcu, name='update link-substation-dcu columns'),
    path('substation-feeder/', views.substation_feeder, name='update link-substation-feeder columns'),
    path('dcu-sim/', views.dcu_sim, name='update link-dcu-sim columns'),
    path('dcu-meter/', views.dcu_meter_config, name='update link-dcu-meter columns'),
    path('feeder-meter/', views.feeder_meter, name='update link-feeder-meter columns'),

    ]



