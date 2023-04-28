from rest_framework import generics, views
from .serializers import *


# Create your views here.

class Substation(generics.ListAPIView):
    queryset = RsmSubstationMaster.objects.filter(DELETE_STATUS=0).all()
    serializer_class = SubstationSerializer


class Substation_DCU(generics.ListAPIView):
    queryset = RsmLinkSubstationDcu.objects.filter(DELETE_STATUS=0).all()
    serializer_class = Substation_DCUSerializer


class Substation_Feeder(generics.ListAPIView):
    queryset = RsmLinkSubstationFeeder.objects.filter(DELETE_STATUS=0).all()
    serializer_class = Substation_FeederSerializer


class DCU(generics.ListAPIView):
    queryset = RsmDcuMaster.objects.filter(DELETE_STATUS=0).all()
    serializer_class = DCUSerializer


class DCU_Sim(generics.ListAPIView):
    queryset = RsmLinkDcuSim.objects.filter(DELETE_STATUS=0).all()
    serializer_class = DCU_SimSerializer


class DCU_Meter(generics.ListAPIView):
    queryset = RsmLinkDcuMeterCongif.objects.filter(DELETE_STATUS=0).all()
    serializer_class = DCU_MeterSerializer


class Fedder(generics.ListAPIView):
    queryset = RsmFeederMaster.objects.filter(DELETE_STATUS=0).all()
    serializer_class = FedderSerializer


class Fedder_Meter(generics.ListAPIView):
    queryset = RsmLinkFeederMeter.objects.filter(DELETE_STATUS=0).all()
    serializer_class = Fedder_MeterSerializer


class Sim(generics.ListAPIView):
    queryset = RsmSimMaster.objects.filter(DELETE_STATUS=0).all()
    serializer_class = SimSerializer


class Meter(generics.ListAPIView):
    queryset = RsmMeterMaster.objects.filter(DELETE_STATUS=0).all()
    serializer_class = MeterSerializer


class VirtualGroup(generics.ListAPIView):
    queryset = RsmVirtualGroupMaster.objects.filter(DELETE_STATUS=0).all()
    serializer_class = VirtualGroupSerializer


class VirtualGroup_Meter(generics.ListAPIView):
    queryset = RsmLinkVgMeter.objects.filter(DELETE_STATUS=0).all()
    serializer_class = VirtualGroup_MeterSerializer
