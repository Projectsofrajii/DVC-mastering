from django.db.models import Max
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


# Create your views here.

@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def substation(request):
    if request.method == "POST":
        serializer = SubstationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.data['AUTO_INDEX'] != 1:
            id_num = str(
                int(RsmSubstationMaster.objects.aggregate(Max('SUBSTATION_ID'))["SUBSTATION_ID__max"][2:]) + 1).zfill(5)
            id = RsmSubstationMaster.objects.aggregate(Max('SUBSTATION_ID'))["SUBSTATION_ID__max"][:2] + id_num
            RsmSubstationMaster.objects.filter(SUBSTATION_ID='').update(SUBSTATION_ID=id)
            return Response('Substation Created', status=status.HTTP_201_CREATED)
        else:
            RsmSubstationMaster.objects.filter(SUBSTATION_ID='').update(SUBSTATION_ID='SS00001')
            return Response('Substation Created', status=status.HTTP_201_CREATED)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def dcu_master(request):
    if request.method == "POST":
        serializer = DcuMasterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.data['AUTO_INDEX'] != 1:
            id_num = str(
                int(RsmDcuMaster.objects.aggregate(Max('DCU_ID'))["DCU_ID__max"][3:]) + 1).zfill(5)
            id = RsmDcuMaster.objects.aggregate(Max('DCU_ID'))["DCU_ID__max"][:3] + id_num
            RsmDcuMaster.objects.filter(DCU_ID='').update(DCU_ID=id)
            return Response('DCU Created', status=status.HTTP_201_CREATED)
        else:
            RsmDcuMaster.objects.filter(DCU_ID='').update(DCU_ID='DCU00001')
            return Response('DCU Created', status=status.HTTP_201_CREATED)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def feeder_master(request):
    if request.method == "POST":
        serializer = FeederMasterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.data['AUTO_INDEX'] != 1:
            id_num = str(
                int(RsmFeederMaster.objects.aggregate(Max('FEEDER_ID'))["FEEDER_ID__max"][3:]) + 1).zfill(5)
            id = RsmFeederMaster.objects.aggregate(Max('FEEDER_ID'))["FEEDER_ID__max"][:3] + id_num
            RsmFeederMaster.objects.filter(FEEDER_ID='').update(FEEDER_ID=id)
            return Response('Feeder Created', status=status.HTTP_201_CREATED)
        else:
            RsmFeederMaster.objects.filter(FEEDER_ID='').update(FEEDER_ID='FID00001')
            return Response('Feeder Created', status=status.HTTP_201_CREATED)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def sim_master(request):
    if request.method == "POST":
        serializer = SimMasterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.data['AUTO_INDEX'] != 1:
            id_num = str(
                int(RsmSimMaster.objects.aggregate(Max('SIM_ID'))["SIM_ID__max"][3:]) + 1).zfill(5)
            id = RsmSimMaster.objects.aggregate(Max('SIM_ID'))["SIM_ID__max"][:3] + id_num
            RsmSimMaster.objects.filter(SIM_ID='').update(SIM_ID=id)
            return Response('Sim Created', status=status.HTTP_201_CREATED)
        else:
            RsmSimMaster.objects.filter(SIM_ID='').update(SIM_ID='SIM00001')
            return Response('Sim Created', status=status.HTTP_201_CREATED)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def meter_master(request):
    if request.method == "POST":
        serializer = MeterMasterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.data['AUTO_INDEX'] != 1:
            id_num = str(
                int(RsmMeterMaster.objects.aggregate(Max('METER_ID'))["METER_ID__max"][5:]) + 1).zfill(4)
            id = RsmMeterMaster.objects.aggregate(Max('METER_ID'))["METER_ID__max"][:5] + id_num
            RsmMeterMaster.objects.filter(METER_ID='').update(METER_ID=id)
            return Response('Meter Created', status=status.HTTP_201_CREATED)
        else:
            RsmMeterMaster.objects.filter(METER_ID='').update(METER_ID='MTRID0000')
            return Response('Meter Created', status=status.HTTP_201_CREATED)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def virtual_group_master(request):
    if request.method == "POST":
        serializer = VirtualGroupMasterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.data['AUTO_INDEX'] != 1:
            id_num = str(
                int(RsmVirtualGroupMaster.objects.aggregate(Max('VIRTUAL_GROUP_ID'))["VIRTUAL_GROUP_ID__max"][
                    3:]) + 1).zfill(5)
            id = RsmVirtualGroupMaster.objects.aggregate(Max('VIRTUAL_GROUP_ID'))["VIRTUAL_GROUP_ID__max"][:3] + id_num
            RsmVirtualGroupMaster.objects.filter(VIRTUAL_GROUP_ID='').update(VIRTUAL_GROUP_ID=id)
            meter_id = request.data['METER_ID']
            for i in meter_id:
                RsmLinkVgMeter.objects.create(VIRTUAL_GROUP_ID=id, METER_ID=i, UPDATED_TIMESTAMP=serializer.data['UPDATED_TIMESTAMP'], DELETE_STATUS=serializer.data['DELETE_STATUS'], DELETED_BY=serializer.data['DELETED_BY'])
            return Response('Virtual Group Created with linked to Meter', status=status.HTTP_201_CREATED)
        else:
            RsmVirtualGroupMaster.objects.filter(VIRTUAL_GROUP_ID='').update(VIRTUAL_GROUP_ID='VID00001')
            meter_id = request.data['METER_ID']
            for i in meter_id:
                RsmLinkVgMeter.objects.create(VIRTUAL_GROUP_ID='VID00001', METER_ID=i,
                                              UPDATED_TIMESTAMP=serializer.data['UPDATED_TIMESTAMP'],
                                              DELETE_STATUS=serializer.data['DELETE_STATUS'],
                                              DELETED_BY=serializer.data['DELETED_BY'])
            return Response('Virtual Group Created with linked to Meter', status=status.HTTP_201_CREATED)
