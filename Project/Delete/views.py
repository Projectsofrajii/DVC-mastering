from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import *


# Create your views here.

@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def substation(request):
    if request.method == "POST":
        substation_id = request.data['SUBSTATION_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmSubstationMaster.objects.filter(SUBSTATION_ID=substation_id):
            RsmSubstationMaster.objects.filter(SUBSTATION_ID=substation_id, DELETE_STATUS=0).update(DELETE_STATUS=1,
                                                                                                    DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Substation_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def dcu(request):
    if request.method == "POST":
        dcu_id = request.data['DCU_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmDcuMaster.objects.filter(DCU_ID=dcu_id):
            RsmDcuMaster.objects.filter(DCU_ID=dcu_id, DELETE_STATUS=0).update(DELETE_STATUS=1,
                                                                               DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('DCU_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def feeder(request):
    if request.method == "POST":
        feeder_id = request.data['FEEDER_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmFeederMaster.objects.filter(FEEDER_ID=feeder_id):
            RsmFeederMaster.objects.filter(FEEDER_ID=feeder_id, DELETE_STATUS=0).update(DELETE_STATUS=1,
                                                                                        DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Feeder_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def sim(request):
    if request.method == "POST":
        sim_id = request.data['SIM_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmSimMaster.objects.filter(SIM_ID=sim_id):
            RsmSimMaster.objects.filter(SIM_ID=sim_id, DELETE_STATUS=0).update(DELETE_STATUS=1,
                                                                               DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Sim_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def meter(request):
    if request.method == "POST":
        meter_id = request.data['METER_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmMeterMaster.objects.filter(METER_ID=meter_id):
            RsmMeterMaster.objects.filter(METER_ID=meter_id, DELETE_STATUS=0).update(DELETE_STATUS=1,
                                                                                     DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Meter_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def virtual_group(request):
    if request.method == "POST":
        virtual_group_id = request.data['VIRTUAL_GROUP_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmVirtualGroupMaster.objects.filter(VIRTUAL_GROUP_ID=virtual_group_id):
            RsmVirtualGroupMaster.objects.filter(VIRTUAL_GROUP_ID=virtual_group_id, DELETE_STATUS=0).update(
                DELETE_STATUS=1,
                DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Virtual_Group_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def substation_dcu(request):
    if request.method == "POST":
        substation_id = request.data['SUBSTATION_ID']
        dcu_id = request.data['DCU_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmLinkSubstationDcu.objects.filter(SUBSTATION_ID=substation_id):
            RsmLinkSubstationDcu.objects.filter(SUBSTATION_ID=substation_id, DCU_ID__in=dcu_id, DELETE_STATUS=0).update(
                DELETE_STATUS=1,
                DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Substation_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def substation_feeder(request):
    if request.method == "POST":
        substation_id = request.data['SUBSTATION_ID']
        feeder_id = request.data['FEEDER_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmLinkSubstationFeeder.objects.filter(SUBSTATION_ID=substation_id):
            RsmLinkSubstationFeeder.objects.filter(SUBSTATION_ID=substation_id, FEEDER_ID__in=feeder_id,
                                                   DELETE_STATUS=0).update(
                DELETE_STATUS=1,
                DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Substation_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def dcu_sim(request):
    if request.method == "POST":
        dcu_id = request.data['DCU_ID']
        sim_id = request.data['SIM_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmLinkDcuSim.objects.filter(DCU_ID=dcu_id):
            RsmLinkDcuSim.objects.filter(DCU_ID=dcu_id, SIM_ID__in=sim_id, DELETE_STATUS=0).update(
                DELETE_STATUS=1,
                DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('DCU_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def dcu_meter_config(request):
    if request.method == "POST":
        dcu_id = request.data['DCU_ID']
        meter_id = request.data['METER_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmLinkDcuMeterCongif.objects.filter(DCU_ID=dcu_id):
            RsmLinkDcuMeterCongif.objects.filter(DCU_ID=dcu_id, METER_ID__in=meter_id, DELETE_STATUS=0).update(
                DELETE_STATUS=1,
                DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('DCU_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def feeder_meter(request):
    if request.method == "POST":
        feeder_id = request.data['FEEDER_ID']
        meter_id = request.data['METER_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmLinkFeederMeter.objects.filter(FEEDER_ID=feeder_id):
            RsmLinkFeederMeter.objects.filter(FEEDER_ID=feeder_id, METER_ID__in=meter_id, DELETE_STATUS=0).update(
                DELETE_STATUS=1,
                DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Feeder_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def virtual_group_meter(request):
    if request.method == "POST":
        virtual_group_id = request.data['VIRTUAL_GROUP_ID']
        meter_id = request.data['METER_ID']
        deleted_by = request.data['DELETED_BY']
        if RsmLinkVgMeter.objects.filter(VIRTUAL_GROUP_ID=virtual_group_id):
            RsmLinkVgMeter.objects.filter(VIRTUAL_GROUP_ID=virtual_group_id, METER_ID__in=meter_id, DELETE_STATUS=0).update(
                DELETE_STATUS=1,
                DELETED_BY=deleted_by)
            return Response('Deleted Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Feeder_id does not exists', status=status.HTTP_404_NOT_FOUND)


