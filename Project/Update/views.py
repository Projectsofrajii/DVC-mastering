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
        substation_name = request.data['SUBSTATION_NAME']
        state_code = request.data['STATE_CODE']
        circle = request.data['CIRCLE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmSubstationMaster.objects.filter(SUBSTATION_ID=substation_id):
            RsmSubstationMaster.objects.filter(SUBSTATION_ID=substation_id).update(SUBSTATION_NAME=substation_name,
                                                                                   STATE_CODE=state_code, CIRCLE=circle,
                                                                                   UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Substation_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def dcu(request):
    if request.method == "POST":
        dcu_id = request.data['DCU_ID']
        dcu_serial_no = request.data['DCU_SERIAL_NO']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmDcuMaster.objects.filter(DCU_ID=dcu_id):
            RsmDcuMaster.objects.filter(DCU_ID=dcu_id).update(DCU_SERIAL_NO=dcu_serial_no,
                                                              UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('DCU_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def feeder(request):
    if request.method == "POST":
        feeder_id = request.data['FEEDER_ID']
        feeder_name = request.data['FEEDER_NAME']
        feeder_type = request.data['FEEDER_TYPE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmFeederMaster.objects.filter(FEEDER_ID=feeder_id):
            RsmFeederMaster.objects.filter(FEEDER_ID=feeder_id).update(FEEDER_NAME=feeder_name, FEEDER_TYPE=feeder_type,
                                                                       UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Feeder_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def sim(request):
    if request.method == "POST":
        sim_id = request.data['SIM_ID']
        sim_no = request.data['SIM_NO']
        mobile_no = request.data['MOBILE_NO']
        imsi = request.data['IMSI']
        gsm_provider = request.data['GSM_PROVIDER']
        sim_type = request.data['SIM_TYPE']
        procured_date = request.data['PROCURED_DATE']
        activate_date = request.data['ACTIVATED_DATE']
        deactivated_date = request.data['DEACTIVATED_DATE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmSimMaster.objects.filter(SIM_ID=sim_id):
            RsmSimMaster.objects.filter(SIM_ID=sim_id).update(SIM_NO=sim_no, MOBILE_NO=mobile_no, IMSI=imsi,
                                                              GSM_PROVIDER=gsm_provider, SIM_TYPE=sim_type,
                                                              PROCURED_DATE=procured_date, ACTIVATED_DATE=activate_date,
                                                              DEACTIVATED_DATE=deactivated_date,
                                                              UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Sim_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def meter(request):
    if request.method == "POST":
        meter_id = request.data['METER_ID']
        meter_serial_no = request.data['METER_SERIAL_NUMBER']
        meter_name = request.data['METER_NAME']
        commissioning_date = request.data['COMMISSIONING_DATE']
        decommissioning_date = request.data['DECOMMISSIONING_DATE']
        meter_static_ip = request.data['METER_STATIC_IP']
        meter_subnet = request.data['METER_SUBNET']
        manufacturer_name = request.data['MANUFACTURER_NAME']
        meter_model = request.data['METER_MODEL']
        firmware_version = request.data['FIRMWARE_VERSION']
        meter_type = request.data['METER_TYPE']
        ct_ratio = request.data['CT_RATIO']
        pt_ratio = request.data['PT_RATIO']
        year_of_manufacture = request.data['YEAR_OF_MANUFACTURE']
        meter_category = request.data['METER_CATEGORY']
        current_rating = request.data['CURRENT_RATING']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmMeterMaster.objects.filter(METER_ID=meter_id):
            RsmMeterMaster.objects.filter(METER_ID=meter_id).update(METER_SERIAL_NUMBER=meter_serial_no,
                                                                    METER_NAME=meter_name,
                                                                    COMMISSIONING_DATE=commissioning_date,
                                                                    DECOMMISSIONING_DATE=decommissioning_date,
                                                                    METER_STATIC_IP=meter_static_ip,
                                                                    METER_SUBNET=meter_subnet,
                                                                    MANUFACTURER_NAME=manufacturer_name,
                                                                    METER_MODEL=meter_model,
                                                                    FIRMWARE_VERSION=firmware_version,
                                                                    METER_TYPE=meter_type, CT_RATIO=ct_ratio,
                                                                    PT_RATIO=pt_ratio,
                                                                    YEAR_OF_MANUFACTURE=year_of_manufacture,
                                                                    METER_CATEGORY=meter_category,
                                                                    CURRENT_RATING=current_rating,
                                                                    UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Meter_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def virtual_group(request):
    if request.method == "POST":
        virtual_group_id = request.data['VIRTUAL_GROUP_ID']
        virtual_group_name = request.data['VIRTUAL_GROUP_NAME']
        description = request.data['DESCRIPTION']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmVirtualGroupMaster.objects.filter(VIRTUAL_GROUP_ID=virtual_group_id):
            RsmVirtualGroupMaster.objects.filter(VIRTUAL_GROUP_ID=virtual_group_id).update(
                VIRTUAL_GROUP_NAME=virtual_group_name, DESCRIPTION=description, UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Virtual_Group_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def substation_dcu(request):
    if request.method == "POST":
        substation_id = request.data['SUBSTATION_ID']
        dcu_id = request.data['DCU_ID']
        commissioning_date = request.data['COMMISSIONING_DATE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmLinkSubstationDcu.objects.filter(SUBSTATION_ID=substation_id):
            RsmLinkSubstationDcu.objects.filter(SUBSTATION_ID=substation_id, DCU_ID__in=dcu_id).update(
                COMMISSIONING_DATE=commissioning_date, UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Substation_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def substation_feeder(request):
    if request.method == "POST":
        substation_id = request.data['SUBSTATION_ID']
        feeder_id = request.data['FEEDER_ID']
        commissioning_date = request.data['COMMISSIONING_DATE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmLinkSubstationFeeder.objects.filter(SUBSTATION_ID=substation_id):
            RsmLinkSubstationFeeder.objects.filter(SUBSTATION_ID=substation_id, FEEDER_ID__in=feeder_id).update(
                COMMISSIONING_DATE=commissioning_date, UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Substation_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def dcu_sim(request):
    if request.method == "POST":
        dcu_id = request.data['DCU_ID']
        sim_id = request.data['SIM_ID']
        slot_no = request.data['SLOT_NO']
        commissioning_date = request.data['COMMISSIONING_DATE']
        decommissioning_date = request.data['DECOMMISSIONING_DATE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmLinkDcuSim.objects.filter(DCU_ID=dcu_id):
            RsmLinkDcuSim.objects.filter(DCU_ID=dcu_id, SIM_ID__in=sim_id).update(SLOT_NO=slot_no,
                                                                                  COMMISSIONING_DATE=commissioning_date,
                                                                                  DECOMMISSIONING_DATE=decommissioning_date,
                                                                                  UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('DCU_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def dcu_meter_config(request):
    if request.method == "POST":
        dcu_id = request.data['DCU_ID']
        meter_id = request.data['METER_ID']
        dcu_ip = request.data['DCU_IP']
        commissioning_date = request.data['COMMISSIONING_DATE']
        dcu_subnet = request.data['DCU_SUBNET']
        meter_ip = request.data['METER_IP']
        meter_subnet = request.data['METER_SUBNET']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmLinkDcuMeterCongif.objects.filter(DCU_ID=dcu_id):
            RsmLinkDcuMeterCongif.objects.filter(DCU_ID=dcu_id, METER_ID__in=meter_id).update(DCU_IP=dcu_ip,
                                                                                              COMMISSIONING_DATE=commissioning_date,
                                                                                              DCU_SUBNET=dcu_subnet,
                                                                                              METER_IP=meter_ip,
                                                                                              METER_SUBNET=meter_subnet,
                                                                                              UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('DCU_id does not exists', status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@permission_classes([AllowAny, ])
@api_view(['POST'])
def feeder_meter(request):
    if request.method == "POST":
        feeder_id = request.data['FEEDER_ID']
        meter_id = request.data['METER_ID']
        meter_mode = request.data['METER_MODE']
        commissioning_date = request.data['COMMISSIONING_DATE']
        updated_timestamp = request.data['UPDATED_TIMESTAMP']
        if RsmLinkFeederMeter.objects.filter(FEEDER_ID=feeder_id):
            RsmLinkFeederMeter.objects.filter(FEEDER_ID=feeder_id, METER_ID__in=meter_id).update(METER_MODE=meter_mode,
                                                                                                 COMMISSIONING_DATE=commissioning_date,
                                                                                                 UPDATED_TIMESTAMP=updated_timestamp)
            return Response('Updated Successfully', status=status.HTTP_202_ACCEPTED)
        else:
            return Response('Feeder_id does not exists', status=status.HTTP_404_NOT_FOUND)
