from rest_framework import serializers
from .models import *


class SubstationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmSubstationMaster
        fields = '__all__'


class DcuMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmDcuMaster
        fields = '__all__'


class FeederMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmFeederMaster
        fields = '__all__'


class SimMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmSimMaster
        fields = '__all__'


class MeterMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmMeterMaster
        fields = '__all__'


class VirtualGroupMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmVirtualGroupMaster
        fields = '__all__'

