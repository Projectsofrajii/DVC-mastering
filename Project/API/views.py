from django.http import JsonResponse
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Prefetch
from django.http import HttpResponse
from django.conf import settings

from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import views
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Subquery, OuterRef

from .models import *
from .serializers import *

cursor = connection.cursor()

from django.utils import timezone
from datetime import datetime, timedelta
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def joins(request):
    with connection.cursor() as cursor:
        try:
            KEY = settings.SECURE_KEY
            if KEY == request.headers['KEY']:
                query = "SELECT mm.METER_ID, mm.METER_SERIAL_NUMBER,max(01_00_5E_5B_00_FF.00_00_01_00_00_FF) as 'Instantaneous',max(01_00_63_01_00_FF.00_00_01_00_00_FF) as 'Block Load Profile',max(01_00_63_02_00_FF.00_00_01_00_00_FF) as 'Daily Load Profile',count(`01_00_5E_5B_00_FF`.`00_00_01_00_00_FF`) as 'Instantaneous Count',count(`01_00_63_01_00_FF`.`00_00_01_00_00_FF`) as 'Block Load Profile Count',count(`01_00_63_02_00_FF`.`00_00_01_00_00_FF`) as 'Daily Load Profile Count' FROM RSM_METER_MASTER mm LEFT JOIN 01_00_5E_5B_00_FF on 01_00_5E_5B_00_FF.METER_ID = mm.METER_ID LEFT JOIN 01_00_63_01_00_FF on 01_00_63_01_00_FF.METER_ID = mm.METER_ID LEFT JOIN 01_00_63_02_00_FF on 01_00_63_02_00_FF.METER_ID = mm.METER_ID GROUP BY mm.METER_ID"
                cursor.execute(query)
                result = dictfetchall(cursor)
                cursor.close()
                return JsonResponse(result, content_type="application/json", safe=False)
            else:
                return JsonResponse({"Message": "Authentication credentials were not provided."})
        except KeyError:
            return JsonResponse({"Message": "Authentication credentials were not provided."})
class timecheck(views.APIView):

    def get(self, request):
        try:
            KEY = settings.SECURE_KEY
            if KEY == request.headers['KEY']:
                queryset = RsmMeterMaster.objects.all()
                serializer_class = MeterSerializer(queryset,many=True)
                return JsonResponse(serializer_class.data,safe=False)
            else:
                return JsonResponse({"Message": "Authentication credentials were not provided."})
        except KeyError:
            return JsonResponse({"Message": "Authentication credentials were not provided."})

class DataLatest(views.APIView):

    def get(self, request):
        try:
            KEY = settings.SECURE_KEY
            if KEY == request.headers['KEY']:
                rsm = RsmMeterMaster.objects.all()
                record_count = rsm.count()
                queryset = RsmMeterMaster.objects.prefetch_related(
                    Prefetch('instant_models', queryset=b01005E5B00Ff.objects.order_by('-_00_00_01_00_00_FF'),
                             to_attr='instant_records'),
                    Prefetch('block_models', queryset=c0100630100Ff.objects.order_by('-_00_00_01_00_00_FF'),
                             to_attr='block_records'),
                    Prefetch('daily_models', queryset=d0100630200Ff.objects.order_by('-_00_00_01_00_00_FF'),
                             to_attr='daily_records')
                ).all()
                latest_records=[]
                for pk in queryset:
                    if pk.instant_records:
                        ins_serializer = InstantSeri(pk.instant_records[0])

                    if pk.block_records:
                        block_serializer = BlockloadSeri(pk.block_records[0])

                    if pk.daily_records:
                        daily_serializer = DailyloadSeri(pk.daily_records[0])

                    latest_records.append({
                                "meter_id": pk.meter_id,
                                "meter_serial_number": pk.meter_serial_number,
                                **(ins_serializer.data if ins_serializer else {"InstantProfile": None}),
                                **(block_serializer.data if block_serializer else {"BlockloadProfile": None}),
                                **(daily_serializer.data if daily_serializer else {"DailyloadProfile": None}),
                            })
                return JsonResponse({
                    "Total Meters": record_count,
                    "latest_records":latest_records
                }, safe=False)
            else:
                return Response({"Detail": "Authentication credentials were not provided."})
        except KeyError:
            return Response({"Detail": "Authentication credentials were not provided."})
class DataAnalysis(views.APIView):

    def get(self, request):
        try:
            KEY = settings.SECURE_KEY
            if KEY == request.headers['KEY']:
                rsm = RsmMeterMaster.objects.all()
                record_count = rsm.count()
                queryset = RsmMeterMaster.objects.prefetch_related(
                    Prefetch('instant_models', queryset=b01005E5B00Ff.objects.order_by('-_00_00_01_00_00_FF'),
                             to_attr='instant_records'),
                    Prefetch('block_models', queryset=c0100630100Ff.objects.order_by('-_00_00_01_00_00_FF'),
                             to_attr='block_records'),
                    Prefetch('daily_models', queryset=d0100630200Ff.objects.order_by('-_00_00_01_00_00_FF'),
                             to_attr='daily_records')
                ).all()

                available_data = 0
                instant_count = 0
                block_count = 0
                daily_count = 0
                null_data_count = 0
                ins_available_data_100 = 0
                block_available_data_100 = 0
                daily_available_data_100 = 0
                inspartialdata = 0
                blockpartialdata = 0
                dailypartialdata = 0

                for pk in queryset:
                    if pk.instant_records:
                        instant_count += 1
                        ins_serializer = InstantSeri(pk.instant_records[0])
                        ins_data = ins_serializer.data
                        ins_values = list(ins_data.values())

                        time = timezone.now()
                        instant_time = ins_values[0]
                        time_format = "%Y-%m-%d %H:%M:%S"
                        ins_time = datetime.strptime(str(instant_time), time_format)
                        time_difference = time - ins_time
                        time_difference_str = time_difference.total_seconds()
                        if time_difference_str <= 1800:
                            ins_available_data_100 += 1
                        else:
                            inspartialdata += 1

                    if pk.block_records:
                        block_count += 1
                        block_serializer = BlockloadSeri(pk.block_records[0])
                        block_data = block_serializer.data
                        block_values = list(block_data.values())

                        time = timezone.now()
                        block_time = block_values[0]
                        time_format = "%Y-%m-%d %H:%M:%S"
                        block_time = datetime.strptime(str(block_time), time_format)
                        time_difference = time - block_time
                        time_difference_str = time_difference.total_seconds()
                        if time_difference_str <= 1800:
                            block_available_data_100 += 1
                        else:
                            blockpartialdata += 1

                    if pk.daily_records:
                        daily_count += 1
                        daily_serializer = DailyloadSeri(pk.daily_records[0])
                        daily_data = daily_serializer.data
                        daily_values = list(daily_data.values())

                        time = timezone.now()
                        daily_time = daily_values[0]
                        time_format = "%Y-%m-%d %H:%M:%S"
                        daily_time = datetime.strptime(str(daily_time), time_format)
                        time_difference = time - daily_time
                        time_difference_str = time_difference.total_seconds()
                        if time_difference_str <= 1800:
                            daily_available_data_100 += 1
                        else:
                            dailypartialdata += 1

                    if pk.instant_records and pk.block_records and pk.daily_records:
                        available_data += 1
                    else:
                        null_data_count += 1
                '''latest_records.append({
                                        "meter_id": pk.meter_id,
                                        "meter_serial_number": pk.meter_serial_number,
                                        **(ins_serializer.data if ins_serializer else {"InstantProfile": None}),
                                        "Instant Time Difference in seconds": time_difference_str if ins_serializer else None,
                                        **(block_serializer.data if block_serializer else {"BlockloadProfile": None}),
                                        **(daily_serializer.data if daily_serializer else {"DailyloadProfile": None}),
                                    })'''
                return JsonResponse({
                    "Total Meters": record_count,
                    "Instant Available Data 100%  ": ins_available_data_100,
                    "Instant Available Data 50%": inspartialdata,
                    "Block Available Data 100%  ": block_available_data_100,
                    "Block Available Data 50%": blockpartialdata,
                    "Daily Available Data 100%  ": daily_available_data_100,
                    "Daily Available Data 50%": dailypartialdata,
                    "Instant data count": instant_count,
                    "Block data count": block_count,
                    "Daily data count": daily_count,
                    "Data not available": null_data_count,
                }, safe=False)
            else:
                return Response({"Detail": "Authentication credentials were not provided."})
        except KeyError:
            return Response({"Detail": "Authentication credentials were not provided."})


class InstantData(views.APIView):#in 16-24 seconds(but server taking(4sec) when removed (block model,daily model entirely)
    def get(self, request):
        try:
            KEY = settings.SECURE_KEY
            if KEY == request.headers['KEY']:
                rsm = RsmMeterMaster.objects.all()
                record_count = rsm.count()
                queryset = RsmMeterMaster.objects.prefetch_related(
                    Prefetch('instant_models', queryset=b01005E5B00Ff.objects.order_by('-_00_00_01_00_00_FF'),
                             to_attr='instant_records')
                ).all()

                instant_count = 0
                null_data_count = 0
                available_data_100 = 0
                partialdata = 0

                for pk in queryset:
                    if pk.instant_records:
                        instant_count += 1
                        ins_serializer = InstantSeri(pk.instant_records[0])
                        ins_data = ins_serializer.data
                        ins_values = list(ins_data.values())

                        time = timezone.now()
                        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                        instant_time = ins_values[0]
                        time_format = "%Y-%m-%d %H:%M:%S"
                        ins_time = datetime.strptime(str(instant_time), time_format)
                        time_difference = time - ins_time
                        time_difference_str = time_difference.total_seconds()
                        if time_difference_str <= 1800:
                            available_data_100 += 1
                        else:
                            partialdata += 1
                    else:
                        null_data_count += 1

                return JsonResponse({
                    "Total Meters": record_count,
                    "Instant Available Data 100%  ": available_data_100,
                    "Instant Available Data 50%": partialdata,
                    "Instant data count": instant_count,
                    "Data not available": null_data_count,
                }, safe=False)
            else:
                return Response({"Detail": "Authentication credentials were not provided."})
        except KeyError:
            return Response({"Detail": "Authentication credentials were not provided."})

@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny, ])
def Retrieve(request, table_code, meter, col_code, date_from='', date_to=''):
    try:
        KEY = settings.SECURE_KEY
        if KEY == request.headers['KEY']:
            if table_code == '00_00_5E_5B_0A_FF':
                try:
                    column_name = col_code.split(',')
                    meter_id = meter.split(',')
                    queryset = a00005E5B0AFf.objects.filter(meter_id__in=meter_id).values('meter_id', *column_name)
                    return Response(queryset, status=status.HTTP_200_OK)
                except ObjectDoesNotExist:
                    res = {"error": "Please select valid credentials"}
                    return Response(res, status=status.HTTP_403_FORBIDDEN)
            elif table_code == '01_00_5E_5B_00_FF':
                try:
                    column_name = col_code.split(',')
                    col = []
                    for i in column_name:
                        col += ['_' + i]
                    date_from = date_from
                    date_to = date_to
                    meter_id = meter.split(',')
                    queryset = b01005E5B00Ff.objects.annotate(meter_serial_number=Subquery(RsmMeterMaster.objects.filter(meter_id=OuterRef('meter_id')).values('meter_serial_number'))).filter(meter_id__in=meter_id,
                                                            _00_00_01_00_00_FF__range=(date_from, date_to)).values(
                        'meter_id', 'meter_serial_number', *col)
                    return Response(queryset, status=status.HTTP_200_OK)
                except ObjectDoesNotExist:
                    res = {"error": "Please select valid credentials"}
                    return Response(res, status=status.HTTP_403_FORBIDDEN)
            elif table_code == '01_00_63_01_00_FF':
                try:
                    column_name = col_code.split(',')
                    col = []
                    for i in column_name:
                        col += ['_' + i]
                    date_from = date_from
                    date_to = date_to
                    meter_id = meter.split(',')
                    queryset = c0100630100Ff.objects.annotate(meter_serial_number=Subquery(RsmMeterMaster.objects.filter(meter_id=OuterRef('meter_id')).values('meter_serial_number'))).filter(meter_id__in=meter_id,
                                                            _00_00_01_00_00_FF__range=(date_from, date_to)).values(
                        'meter_id', 'meter_serial_number', *col)
                    return Response(queryset, status=status.HTTP_200_OK)
                except ObjectDoesNotExist:
                    res = {"error": "Please select valid credentials"}
                    return Response(res, status=status.HTTP_403_FORBIDDEN)
            elif table_code == '01_00_63_02_00_FF':
                try:
                    column_name = col_code.split(',')
                    col = []
                    for i in column_name:
                        col += ['_' + i]
                    date_from = date_from
                    date_to = date_to
                    meter_id = meter.split(',')
                    queryset = d0100630200Ff.objects.annotate(meter_serial_number=Subquery(RsmMeterMaster.objects.filter(meter_id=OuterRef('meter_id')).values('meter_serial_number'))).filter(meter_id__in=meter_id,
                                                            _00_00_01_00_00_FF__range=(date_from, date_to)).values(
                        'meter_id', 'meter_serial_number', *col)
                    return Response(queryset, status=status.HTTP_200_OK)
                except ObjectDoesNotExist:
                    res = {"error": "Please select valid credentials"}
                    return Response(res, status=status.HTTP_403_FORBIDDEN)

            else:
                res = {'Error': 'Please provide valid table name'}
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        else:
            return HttpResponse("Authentication credentials were not provided.")
    except KeyError:
        res = {"Error": "Authentication credentials were not provided."}
        return Response(res, status=status.HTTP_403_FORBIDDEN)


@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny, ])
def description(request, table_code):
    try:
        KEY = settings.SECURE_KEY
        if KEY == request.headers['KEY']:
            if table_code == '00_00_5E_5B_0A_FF':
                queryset = RsmOcTableCoulumns.objects.filter(table_code=table_code).values('column_code')
                dic = {}
                for i in queryset.values_list('column_code'):
                    queryset = RsmColumnObisCode.objects.filter(hex_oc=i[0]).values('description')
                    dic.update({i[0]: queryset})
                return Response(dic)
            elif table_code == '01_00_5E_5B_00_FF':
                queryset = RsmOcTableCoulumns.objects.filter(table_code=table_code).values('column_code')
                dic = {}
                for i in queryset.values_list('column_code'):
                    queryset = RsmColumnObisCode.objects.filter(hex_oc=i[0]).values('description')
                    dic.update({i[0]: queryset})
                return Response(dic)
            elif table_code == '01_00_63_01_00_FF':
                queryset = RsmOcTableCoulumns.objects.filter(table_code=table_code).values('column_code')
                dic = {}
                for i in queryset.values_list('column_code'):
                    queryset = RsmColumnObisCode.objects.filter(hex_oc=i[0]).values('description')
                    dic.update({i[0]: queryset})
                return Response(dic)
            elif table_code == '01_00_63_02_00_FF':
                queryset = RsmOcTableCoulumns.objects.filter(table_code=table_code).values('column_code')
                dic = {}
                for i in queryset.values_list('column_code'):
                    queryset = RsmColumnObisCode.objects.filter(hex_oc=i[0]).values('description')
                    dic.update({i[0]: queryset})
                return Response(dic)
            else:
                res = {'Error': 'Please provide valid table name'}
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        else:
            return HttpResponse("Authentication credentials were not provided.")
    except KeyError:
        res = {"Error": "Authentication credentials were not provided."}
        return Response(res, status=status.HTTP_403_FORBIDDEN)


class Meter_Retrieve(views.APIView):
    def get(self, request):
        try:
            KEY = settings.SECURE_KEY
            if KEY == request.headers['KEY']:
                queryset = RsmMeterMaster.objects.all()
                serializer_class = MeterSerializer(queryset, many=True)
                return Response({"Detail": serializer_class.data})
            else:
                return Response({"Detail": "Authentication credentials were not provided."})
        except KeyError:
            res = {"Error": "Authentication credentials were not provided."}
            return Response(res, status=status.HTTP_403_FORBIDDEN)


class Table_desc(views.APIView):
    def get(self, request):
        try:
            KEY = settings.SECURE_KEY
            if KEY == request.headers['KEY']:
                queryset = RsmTableObisCode.objects.all()
                serializer_class = RTOCSerializer(queryset, many=True)
                return Response({"Detail": serializer_class.data})
            else:
                return Response({"Detail": "Authentication credentials were not provided."})
        except KeyError:
            res = {"Error": "Authentication credentials were not provided."}
            return Response(res, status=status.HTTP_403_FORBIDDEN)

class Ins(views.APIView):
    def get(self, request):
        try:
            KEY = settings.SECURE_KEY
            if KEY == request.headers['KEY']:
                queryset = b01005E5B00Ff.objects.all()
                serializer_class = InstantSeri(queryset, many=True)
                return Response({"Detail": serializer_class.data})
            else:
                return Response({"Detail": "Authentication credentials were not provided."})
        except KeyError:
            res = {"Error": "Authentication credentials were not provided."}
            return Response(res, status=status.HTTP_403_FORBIDDEN)


class Block(views.APIView):
    def get(self, request):
        try:
            KEY = settings.SECURE_KEY
            if KEY == request.headers['KEY']:
                queryset = c0100630100Ff.objects.all()
                serializer_class = BlockloadSeri(queryset, many=True)
                return Response({"Detail": serializer_class.data})
            else:
                return Response({"Detail": "Authentication credentials were not provided."})
        except KeyError:
            res = {"Error": "Authentication credentials were not provided."}
            return Response(res, status=status.HTTP_403_FORBIDDEN)


class Daily(views.APIView):
    def get(self, request):
        try:
            KEY = settings.SECURE_KEY
            if KEY == request.headers['KEY']:
                queryset = d0100630200Ff.objects.all()
                serializer_class = DailyloadSeri(queryset, many=True)
                return Response({"Detail": serializer_class.data})
            else:
                return Response({"Detail": "Authentication credentials were not provided."})
        except KeyError:
            res = {"Error": "Authentication credentials were not provided."}
            return Response(res, status=status.HTTP_403_FORBIDDEN)


