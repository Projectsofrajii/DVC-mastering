from django.db.models import Max
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
def substation_dcu(request):
    if request.method == "POST":
        auto_index = request.data['AUTO_INDEX']
        substation_id = request.data['SUBSTATION_ID']
        dcu_id = request.data['DCU_ID']
        commissioning_date = request.data['COMMISSIONING_DATE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        delete_status = request.data['DELETE_STATUS']
        delete_by = request.data['DELETED_BY']
        if RsmSubstationMaster.objects.filter(SUBSTATION_ID=substation_id):
            for i in dcu_id:
                RsmLinkSubstationDcu.objects.create(SUBSTATION_ID=substation_id, DCU_ID=i,
                                                    COMMISSIONING_DATE=commissioning_date,
                                                    UPDATED_TIMESTAMP=updated_timestamp,
                                                    DELETE_STATUS=delete_status,
                                                    DELETED_BY=delete_by)
            return Response('Link created', status=status.HTTP_201_CREATED)
        else:
            return Response('SUBSTATION_ID does not exists', status=status.HTTP_201_CREATED)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def substation_feeder(request):
    if request.method == "POST":
        auto_index = request.data['AUTO_INDEX']
        substation_id = request.data['SUBSTATION_ID']
        feeder_id = request.data['FEEDER_ID']
        commissioning_date = request.data['COMMISSIONING_DATE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        delete_status = request.data['DELETE_STATUS']
        delete_by = request.data['DELETED_BY']
        if RsmSubstationMaster.objects.filter(SUBSTATION_ID=substation_id):
            for i in feeder_id:
                RsmLinkSubstationFeeder.objects.create(SUBSTATION_ID=substation_id, FEEDER_ID=i,
                                                       COMMISSIONING_DATE=commissioning_date,
                                                       UPDATED_TIMESTAMP=updated_timestamp,
                                                       DELETE_STATUS=delete_status,
                                                       DELETED_BY=delete_by)
            return Response('Link created', status=status.HTTP_201_CREATED)
        else:
            return Response('SUBSTATION_ID does not exists', status=status.HTTP_201_CREATED)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def dcu_sim(request):
    if request.method == "POST":
        auto_index = request.data['AUTO_INDEX']
        dcu_id = request.data['DCU_ID']
        sim_id = request.data['SIM_ID']
        slot_no = request.data['SLOT_NO']
        decommissioning_date = request.data['DECOMMISSIONING_DATE']
        commissioning_date = request.data['COMMISSIONING_DATE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        delete_status = request.data['DELETE_STATUS']
        delete_by = request.data['DELETED_BY']
        if RsmDcuMaster.objects.filter(DCU_ID=dcu_id):
            for i in sim_id:
                RsmLinkDcuSim.objects.create(DCU_ID=dcu_id, SIM_ID=i, SLOT_NO=slot_no,
                                             DECOMMISSIONING_DATE=decommissioning_date,
                                             COMMISSIONING_DATE=commissioning_date,
                                             UPDATED_TIMESTAMP=updated_timestamp,
                                             DELETE_STATUS=delete_status, DELETED_BY=delete_by)
            return Response('Link created', status=status.HTTP_201_CREATED)
        else:
            return Response('DCU_ID does not exists', status=status.HTTP_201_CREATED)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def dcu_meter(request):
    if request.method == "POST":
        auto_index = request.data['AUTO_INDEX']
        dcu_id = request.data['DCU_ID']
        meter_id = request.data['METER_ID']
        dcu_ip = request.data['DCU_IP']
        dcu_subnet = request.data['DCU_SUBNET']
        meter_ip = request.data['METER_IP']
        meter_subnet = request.data['METER_SUBNET']
        commissioning_date = request.data['COMMISSIONING_DATE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        delete_status = request.data['DELETE_STATUS']
        delete_by = request.data['DELETED_BY']
        if RsmDcuMaster.objects.filter(DCU_ID=dcu_id):
            for i in meter_id:
                RsmLinkDcuMeterCongif.objects.create(DCU_ID=dcu_id, METER_ID=i, DCU_IP=dcu_ip,
                                                     DCU_SUBNET=dcu_subnet,
                                                     METER_IP=meter_ip, METER_SUBNET=meter_subnet,
                                                     COMMISSIONING_DATE=commissioning_date,
                                                     UPDATED_TIMESTAMP=updated_timestamp,
                                                     DELETE_STATUS=delete_status, DELETED_BY=delete_by)
            return Response('Link created', status=status.HTTP_201_CREATED)
        else:
            return Response('DCU_ID does not exists', status=status.HTTP_201_CREATED)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def feeder_meter(request):
    if request.method == "POST":
        auto_index = request.data['AUTO_INDEX']
        feeder_id = request.data['FEEDER_ID']
        meter_id = request.data['METER_ID']
        meter_mode = request.data['METER_MODE']
        commissioning_date = request.data['COMMISSIONING_DATE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        delete_status = request.data['DELETE_STATUS']
        delete_by = request.data['DELETED_BY']
        if RsmFeederMaster.objects.filter(FEEDER_ID=feeder_id):
            for i in meter_id:
                RsmLinkFeederMeter.objects.create(FEEDER_ID=feeder_id, METER_ID=i, METER_MODE=meter_mode,
                                                  COMMISSIONING_DATE=commissioning_date,
                                                  UPDATED_TIMESTAMP=updated_timestamp,
                                                  DELETE_STATUS=delete_status,
                                                  DELETED_BY=delete_by)
            return Response('Link created', status=status.HTTP_201_CREATED)
        else:
            return Response('FEEDER_ID does not exists', status=status.HTTP_201_CREATED)
