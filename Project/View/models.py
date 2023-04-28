from django.db import models
from datetime import datetime


# Create your models here.
class RsmSubstationMaster(models.Model):
    AUTO_INDEX = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    SUBSTATION_ID = models.CharField(db_column='SUBSTATION_ID', max_length=8)
    SUBSTATION_NAME = models.CharField(db_column='SUBSTATION_NAME', max_length=64)
    STATE_CODE = models.CharField(db_column='STATE_CODE', max_length=8, blank=True,
                                  null=True)
    CIRCLE = models.CharField(db_column='CIRCLE', max_length=32, blank=True, null=True)
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP')
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8, default=1)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RSM_SUBSTATION_MASTER'


class RsmLinkSubstationDcu(models.Model):
    AUTO_INDEX = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    SUBSTATION_ID = models.CharField(db_column='SUBSTATION_ID', max_length=8)
    DCU_ID = models.CharField(db_column='DCU_ID', max_length=8)
    COMMISSIONING_DATE = models.DateTimeField(db_column='COMMISSIONING_DATE')
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP', default=datetime.now)
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8, default=1)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True,
                                  null=True, default='')

    class Meta:
        managed = False
        db_table = 'RSM_LINK_SUBSTATION_DCU'


class RsmLinkSubstationFeeder(models.Model):
    AUTO_INDEX = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    SUBSTATION_ID = models.CharField(db_column='SUBSTATION_ID', max_length=8)
    FEEDER_ID = models.CharField(db_column='FEEDER_ID', max_length=8)
    COMMISSIONING_DATE = models.DateTimeField(db_column='COMMISSIONING_DATE')
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP', default=datetime.now)
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8, default=1)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True,
                                  null=True, default='')

    class Meta:
        managed = False
        db_table = 'RSM_LINK_SUBSTATION_FEEDER'


class RsmDcuMaster(models.Model):
    DCU_ID = models.CharField(db_column='DCU_ID', primary_key=True, max_length=16, default='')
    DCU_SERIAL_NO = models.CharField(db_column='DCU_SERIAL_NO', max_length=16)
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP')
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True,
                                  null=True)

    class Meta:
        managed = False
        db_table = 'RSM_DCU_MASTER'


class RsmLinkDcuSim(models.Model):
    AUTO_INDEX = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    DCU_ID = models.CharField(db_column='DCU_ID', max_length=16)
    SIM_ID = models.CharField(db_column='SIM_ID', max_length=16)
    SLOT_NO = models.CharField(db_column='SLOT_NO', max_length=8)
    COMMISSIONING_DATE = models.DateTimeField(db_column='COMMISSIONING_DATE')
    DECOMMISSIONING_DATE = models.DateTimeField(db_column='DECOMMISSIONING_DATE')
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP', default=datetime.now)
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8, default=1)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True,
                                  null=True, default='')

    class Meta:
        managed = False
        db_table = 'RSM_LINK_DCU_SIM'


class RsmLinkDcuMeterCongif(models.Model):
    AUTO_INDEX = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    DCU_ID = models.CharField(db_column='DCU_ID', max_length=8)
    METER_ID = models.CharField(db_column='METER_ID', max_length=16)
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP')
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True, null=True)
    DCU_IP = models.CharField(db_column='DCU_IP', max_length=32)
    DCU_SUBNET = models.CharField(db_column='DCU_SUBNET', max_length=32)
    METER_IP = models.CharField(db_column='METER_IP', max_length=32)
    METER_SUBNET = models.CharField(db_column='METER_SUBNET', max_length=32)
    COMMISSIONING_DATE = models.DateTimeField(db_column='COMMISSIONING_DATE')

    class Meta:
        managed = False
        db_table = 'RSM_LINK_DCU_METER_CONGIF'


class RsmFeederMaster(models.Model):
    AUTO_INDEX = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    FEEDER_ID = models.CharField(db_column='FEEDER_ID', max_length=8, default='')
    FEEDER_NAME = models.CharField(db_column='FEEDER_NAME', max_length=64)
    FEEDER_TYPE = models.CharField(db_column='FEEDER_TYPE', max_length=32)
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP')
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RSM_FEEDER_MASTER'


class RsmLinkFeederMeter(models.Model):
    AUTO_INDEX = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    FEEDER_ID = models.CharField(db_column='FEEDER_ID', max_length=8)
    METER_ID = models.CharField(db_column='METER_ID', max_length=16)
    COMMISSIONING_DATE = models.DateTimeField(db_column='COMMISSIONING_DATE')
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP')
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True,
                                  null=True)

    class Meta:
        managed = False
        db_table = 'RSM_LINK_FEEDER_METER'


class RsmSimMaster(models.Model):
    SIM_ID = models.CharField(db_column='SIM_ID', primary_key=True, max_length=8, default='')
    SIM_NO = models.IntegerField(db_column='SIM_NO')
    MOBILE_NO = models.IntegerField(db_column='MOBILE_NO')
    IMSI = models.CharField(db_column='IMSI', max_length=32)
    GSM_PROVIDER = models.CharField(db_column='GSM_PROVIDER', max_length=16)
    SIM_TYPE = models.CharField(db_column='SIM_TYPE', max_length=16)
    PROCURED_DATE = models.DateTimeField(db_column='PROCURED_DATE')
    ACTIVATED_DATE = models.DateTimeField(db_column='ACTIVATED_DATE')
    DEACTIVATED_DATE = models.DateTimeField(db_column='DEACTIVATED_DATE')
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP')
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True,
                                  null=True)

    class Meta:
        managed = False
        db_table = 'RSM_SIM_MASTER'


class RsmMeterMaster(models.Model):
    AUTO_INDEX = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    METER_ID = models.CharField(db_column='METER_ID', max_length=16, default='')
    METER_SERIAL_NUMBER = models.CharField(db_column='METER_SERIAL_NUMBER', max_length=16, blank=True,
                                           null=True)
    METER_NAME = models.CharField(db_column='METER_NAME', max_length=32)
    COMMISSIONING_DATE = models.DateTimeField(db_column='COMMISSIONING_DATE')
    DECOMMISSIONING_DATE = models.DateTimeField(db_column='DECOMMISSIONING_DATE')
    METER_STATIC_IP = models.CharField(db_column='METER_STATIC_IP', max_length=32)
    METER_SUBNET = models.CharField(db_column='METER_SUBNET', max_length=32)
    MANUFACTURER_NAME = models.CharField(db_column='MANUFACTURER_NAME', max_length=45, blank=True,
                                         null=True)
    METER_MODEL = models.CharField(db_column='METER_MODEL', max_length=16)
    FIRMWARE_VERSION = models.CharField(db_column='FIRMWARE_VERSION', max_length=16)
    METER_TYPE = models.CharField(db_column='METER_TYPE', max_length=8)
    CT_RATIO = models.CharField(db_column='CT_RATIO', max_length=8)
    PT_RATIO = models.CharField(db_column='PT_RATIO', max_length=8)
    YEAR_OF_MANUFACTURE = models.CharField(db_column='YEAR_OF_MANUFACTURE', max_length=8)
    METER_CATEGORY = models.CharField(db_column='METER_CATEGORY', max_length=8)
    CURRENT_RATING = models.CharField(db_column='CURRENT_RATING', max_length=8)
    LAST_UPDATED_TIMESTAMP = models.DateTimeField(db_column='LAST_UPDATED_TIMESTAMP')
    DELETE_STATUS = models.IntegerField(db_column='DELETE_STATUS')
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True,
                                  null=True)

    class Meta:
        managed = False
        db_table = 'RSM_METER_MASTER'


class RsmVirtualGroupMaster(models.Model):
    AUTO_INDEX = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    VIRTUAL_GROUP_ID = models.CharField(db_column='VIRTUAL_GROUP_ID', max_length=16, default='')
    VIRTUAL_GROUP_NAME = models.CharField(db_column='VIRTUAL_GROUP_NAME', max_length=16)
    DESCRIPTION = models.CharField(db_column='DESCRIPTION', max_length=64)
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP')
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RSM_VIRTUAL_GROUP_MASTER'


class RsmLinkVgMeter(models.Model):
    AUTO_INDEX = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    VIRTUAL_GROUP_ID = models.CharField(db_column='VIRTUAL_GROUP_ID', max_length=16, default='')
    METER_ID = models.CharField(db_column='METER_ID', max_length=16, default='')
    UPDATED_TIMESTAMP = models.DateTimeField(db_column='UPDATED_TIMESTAMP', default=datetime.now)
    DELETE_STATUS = models.CharField(db_column='DELETE_STATUS', max_length=8, default=1)
    DELETED_BY = models.CharField(db_column='DELETED_BY', max_length=16, blank=True,
                                  null=True, default='')

    class Meta:
        managed = False
        db_table = 'RSM_LINK_VG_METER'
