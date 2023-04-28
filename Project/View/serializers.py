from rest_framework import serializers
from .models import *


class SubstationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmSubstationMaster
        fields = '__all__'


class Substation_DCUSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmLinkSubstationDcu
        fields = '__all__'


class Substation_FeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmLinkSubstationFeeder
        fields = '__all__'


class DCUSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmDcuMaster
        fields = '__all__'


class DCU_SimSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmLinkDcuSim
        fields = '__all__'


class DCU_MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmLinkDcuMeterCongif
        fields = '__all__'


class FedderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmFeederMaster
        fields = '__all__'


class Fedder_MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmLinkFeederMeter
        fields = '__all__'


class SimSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmSimMaster
        fields = '__all__'


class MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmMeterMaster
        fields = '__all__'


class VirtualGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmVirtualGroupMaster
        fields = '__all__'


class VirtualGroup_MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmLinkVgMeter
        fields = '__all__'
