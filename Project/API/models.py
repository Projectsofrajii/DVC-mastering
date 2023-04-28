from django.db import models


class a00005E5B0AFf(models.Model):  # 1 NamePlateProfile
    auto_index = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    meter_id = models.CharField(db_column='METER_ID', max_length=45, blank=True, null=True)
    _00_00_60_01_00_FF = models.CharField(db_column='00_00_60_01_00_FF', max_length=100, blank=True, null=True)
    _00_00_60_01_01_FF = models.CharField(db_column='00_00_60_01_01_FF', max_length=100, blank=True, null=True)
    _01_00_00_02_00_FF = models.CharField(db_column='01_00_00_02_00_FF', max_length=100, blank=True, null=True)
    _00_00_5E_5B_09_FF = models.CharField(db_column='00_00_5E_5B_09_FF', max_length=100, blank=True, null=True)
    _00_00_5E_5B_0b_FF = models.CharField(db_column='00_00_5E_5B_0B_FF', max_length=100, blank=True, null=True)
    _00_00_5E_5B_0c_FF = models.CharField(db_column='00_00_5E_5B_0C_FF', max_length=100, blank=True, null=True)
    _01_00_00_04_02_FF = models.CharField(db_column='01_00_00_04_02_FF', max_length=100, blank=True, null=True)
    _01_00_00_04_03_FF = models.CharField(db_column='01_00_00_04_03_FF', max_length=100, blank=True, null=True)
    _00_00_60_01_04_FF = models.CharField(db_column='00_00_60_01_04_FF', max_length=100, blank=True, null=True)
    updated_timestamp = models.DateTimeField(db_column='UPDATED_TIMESTAMP')

    class Meta:
        managed = False
        db_table = '00_00_5E_5B_0A_FF'


class RsmMeterMaster(models.Model):
    meter_id = models.CharField(db_column='METER_ID', primary_key=True, max_length=45)
    meter_serial_number = models.CharField(db_column='METER_SERIAL_NUMBER', max_length=45, blank=True, null=True)
    manufacturer_name = models.CharField(db_column='MANUFACTURER_NAME', max_length=45, blank=True, null=True)
    firmware_version = models.CharField(db_column='FIRMWARE_VERSION', max_length=100)
    meter_type = models.CharField(db_column='METER_TYPE', max_length=100)
    ct_ratio = models.CharField(db_column='CT_RATIO', max_length=100)
    pt_ratio = models.CharField(db_column='PT_RATIO', max_length=100)
    year_of_manufacture = models.CharField(db_column='YEAR_OF_MANUFACTURE', max_length=100)
    meter_category = models.CharField(db_column='METER_CATEGORY', max_length=100)
    current_rating = models.CharField(db_column='CURRENT_RATING', max_length=100)

    class Meta:
        managed = False
        db_table = 'RSM_METER_MASTER'


class b01005E5B00Ff(models.Model):  # 1 InstantModel
    auto_index = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    meter_id = models.ForeignKey(RsmMeterMaster, db_column='METER_ID', on_delete=models.CASCADE,
                                 related_name='instant_models')
    _00_00_01_00_00_FF = models.CharField(db_column='00_00_01_00_00_FF', max_length=100, blank=True, null=True)
    _01_00_1F_07_00_FF = models.CharField(db_column='01_00_1F_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_33_07_00_FF = models.CharField(db_column='01_00_33_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_47_07_00_FF = models.CharField(db_column='01_00_47_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_21_07_00_FF = models.CharField(db_column='01_00_21_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_35_07_00_FF = models.CharField(db_column='01_00_35_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_49_07_00_FF = models.CharField(db_column='01_00_49_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_0D_07_00_FF = models.CharField(db_column='01_00_0D_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_0E_07_00_FF = models.CharField(db_column='01_00_0E_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_09_07_00_FF = models.CharField(db_column='01_00_09_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_01_07_00_FF = models.CharField(db_column='01_00_01_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_03_07_00_FF = models.CharField(db_column='01_00_03_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_01_08_00_FF = models.CharField(db_column='01_00_01_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_02_08_00_FF = models.CharField(db_column='01_00_02_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_09_08_00_FF = models.CharField(db_column='01_00_09_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_0A_08_00_FF = models.CharField(db_column='01_00_0A_08_00_FF', max_length=100, blank=True, null=True)
    _00_00_60_07_00_FF = models.CharField(db_column='00_00_60_07_00_FF', max_length=100, blank=True, null=True)
    _00_00_5E_5B_08_FF = models.CharField(db_column='00_00_5E_5B_08_FF', max_length=100, blank=True, null=True)
    _00_00_5E_5B_00_FF = models.CharField(db_column='00_00_5E_5B_00_FF', max_length=100, blank=True, null=True)
    _00_00_00_01_00_FF = models.CharField(db_column='00_00_00_01_00_FF', max_length=100, blank=True, null=True)
    _00_00_60_02_00_FF = models.CharField(db_column='00_00_60_02_00_FF', max_length=100, blank=True, null=True)
    _00_00_00_01_02_FF = models.CharField(db_column='00_00_00_01_02_FF', max_length=100, blank=True, null=True)
    _01_00_20_07_00_FF = models.CharField(db_column='01_00_20_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_34_07_00_FF = models.CharField(db_column='01_00_34_07_00_FF', max_length=100, blank=True, null=True)
    _01_00_48_07_00_FF = models.CharField(db_column='01_00_48_07_00_FF', max_length=100, blank=True, null=True)
    updated_timestamp = models.DateTimeField(db_column='UPDATED_TIMESTAMP')

    def __str__(self):
        return self.meter_id

    class Meta:
        managed = False
        db_table = '01_00_5E_5B_00_FF'


class c0100630100Ff(models.Model):  # 2 BlockloadModel
    auto_index = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    meter_id = models.ForeignKey(RsmMeterMaster, db_column='METER_ID', on_delete=models.CASCADE,
                                 related_name='block_models')
    _00_00_01_00_00_FF = models.CharField(db_column='00_00_01_00_00_FF', max_length=100, blank=True, null=True)
    _01_00_01_1D_00_FF = models.CharField(db_column='01_00_01_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_02_1D_00_FF = models.CharField(db_column='01_00_02_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_81_1D_00_FF = models.CharField(db_column='01_00_81_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_82_1D_00_FF = models.CharField(db_column='01_00_82_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_05_1D_00_FF = models.CharField(db_column='01_00_05_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_08_1D_00_FF = models.CharField(db_column='01_00_08_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_06_1D_00_FF = models.CharField(db_column='01_00_06_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_07_1D_00_FF = models.CharField(db_column='01_00_07_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_09_1D_00_FF = models.CharField(db_column='01_00_09_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_0A_1D_00_FF = models.CharField(db_column='01_00_0A_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_10_1D_00_FF = models.CharField(db_column='01_00_10_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_97_1D_00_FF = models.CharField(db_column='01_00_97_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_98_1D_00_FF = models.CharField(db_column='01_00_98_1D_00_FF', max_length=100, blank=True, null=True)
    _01_00_60_05_04_FF = models.CharField(db_column='01_00_60_05_04_FF', max_length=100, blank=True, null=True)
    _01_00_20_1B_00_FF = models.CharField(db_column='01_00_20_1B_00_FF', max_length=100, blank=True, null=True)
    _01_00_34_1B_00_FF = models.CharField(db_column='01_00_34_1B_00_FF', max_length=100, blank=True, null=True)
    _01_00_48_1B_00_FF = models.CharField(db_column='01_00_48_1B_00_FF', max_length=100, blank=True, null=True)
    _01_00_1F_1B_00_FF = models.CharField(db_column='01_00_1F_1B_00_FF', max_length=100, blank=True, null=True)
    _01_00_33_1B_00_FF = models.CharField(db_column='01_00_33_1B_00_FF', max_length=100, blank=True, null=True)
    _01_00_47_1B_00_FF = models.CharField(db_column='01_00_47_1B_00_FF', max_length=100, blank=True, null=True)
    _01_00_0E_1B_00_FF = models.CharField(db_column='01_00_0E_1B_00_FF', max_length=100, blank=True, null=True)
    updated_timestamp = models.DateTimeField(db_column='UPDATED_TIMESTAMP')

    class Meta:
        managed = False
        db_table = '01_00_63_01_00_FF'


class d0100630200Ff(models.Model):  # 3 DailyloadModel
    auto_index = models.AutoField(db_column='AUTO_INDEX', primary_key=True)
    meter_id = models.ForeignKey(RsmMeterMaster, db_column='METER_ID', on_delete=models.CASCADE,
                                 related_name='daily_models')
    _00_00_01_00_00_FF = models.CharField(db_column='00_00_01_00_00_FF', max_length=100, blank=True, null=True)
    _01_00_01_08_00_FF = models.CharField(db_column='01_00_01_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_02_08_00_FF = models.CharField(db_column='01_00_02_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_81_08_00_FF = models.CharField(db_column='01_00_81_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_82_08_00_FF = models.CharField(db_column='01_00_82_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_05_08_00_FF = models.CharField(db_column='01_00_05_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_08_08_00_FF = models.CharField(db_column='01_00_08_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_06_08_00_FF = models.CharField(db_column='01_00_06_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_07_08_00_FF = models.CharField(db_column='01_00_07_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_09_08_00_FF = models.CharField(db_column='01_00_09_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_0A_08_00_FF = models.CharField(db_column='01_00_0A_08_00_FF', max_length=100, blank=True, null=True)
    _01_00_5E_5B_01_FF = models.CharField(db_column='01_00_5E_5B_01_FF', max_length=100, blank=True, null=True)
    _01_00_5E_5B_02_FF = models.CharField(db_column='01_00_5E_5B_02_FF', max_length=100, blank=True, null=True)
    updated_timestamp = models.DateTimeField(db_column='UPDATED_TIMESTAMP')

    class Meta:
        managed = False
        db_table = '01_00_63_02_00_FF'


class RsmTableObisCode(models.Model):
    internal_id = models.CharField(primary_key=True, max_length=10)
    hex_oc = models.CharField(max_length=85)
    decimal_oc = models.CharField(max_length=85)
    description = models.CharField(max_length=200)
    short_name = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'RSM_TABLE_OBIS_CODE'


class RsmOcTableCoulumns(models.Model):
    auto_index = models.IntegerField(primary_key=True)
    column_code = models.CharField(max_length=45)
    table_code = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'RSM_OC_TABLE_COULUMNS'


class RsmColumnObisCode(models.Model):
    internal_id = models.CharField(db_column='INTERNAL_ID', primary_key=True,
                                   max_length=10)  # Field name made lowercase.
    hex_oc = models.CharField(db_column='HEX_OC', max_length=85)  # Field name made lowercase.
    decimal_oc = models.CharField(db_column='DECIMAL_OC', max_length=85)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RSM_COLUMN_OBIS_CODE'
