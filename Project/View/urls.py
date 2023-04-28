from django.urls import path
from . import views

urlpatterns = [
    path('substation/', views.Substation.as_view(), name='Substation Data'),
    path('substation-dcu/', views.Substation_DCU.as_view(), name='Substation-DCU Data'),
    path('substation-feeder/', views.Substation_Feeder.as_view(), name='Substation-Feeder Data'),
    path('dcu/', views.DCU.as_view(), name='DCU Data'),
    path('dcu-sim/', views.DCU_Sim.as_view(), name='DCU-Sim Data'),
    path('dcu-meter/', views.DCU_Meter.as_view(), name='DCU-Meter Data'),
    path('feeder/', views.Fedder.as_view(), name='Feeder Data'),
    path('feeder-meter/', views.Fedder_Meter.as_view(), name='Feeder-Meter Data'),
    path('sim/', views.Sim.as_view(), name='Sim Data'),
    path('meter/', views.Meter.as_view(), name='Meter Data'),
    path('virtualgroup/', views.VirtualGroup.as_view(), name='Virtual-Group Data'),
    path('virtualgroup-meter/', views.VirtualGroup_Meter.as_view(), name='Virtual-Group-Meter Data'),

    ]


