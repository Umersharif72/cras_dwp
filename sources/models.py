from django.db import models
from django.utils import timezone

class SourceConn(models.Model):
    SID = models.AutoField(primary_key=True)  # Assuming SID is auto-generated
    Jurisdiction = models.CharField(max_length=100)
    DATABASES = models.CharField(max_length=100)
    Src_DB_NAME = models.CharField(max_length=100)
    Src_USER_NAME = models.CharField(max_length=100)
    Src_PASSWRD = models.CharField(max_length=100)
    Src_HOST = models.CharField(max_length=100)
    Src_PORT = models.IntegerField()
    Src_UPDATE_TIME = models.DateTimeField(auto_now_add=True)  # Assuming Src_UPDATE_TIME is auto-generated

    class Meta:
        managed = False  # Django won't manage this table as it's already created in the database
        db_table = 'SourceConn'  # Specify the name of your existing table


class c_app_db(models.Model):
    sid = models.AutoField(primary_key=True)  # AutoField for the 'sid' column
    Apps = models.CharField(max_length=255)
    DB_name = models.CharField(max_length=255)
    Update_time = models.DateTimeField(auto_now_add=True)  # AutoField for the 'Update_time' column

    class Meta:
        db_table = 'c_app_db'  # Specify the table name in the database
        managed = False



class ce_mapng(models.Model):
    SID = models.AutoField(primary_key=True)  # Assuming SID is auto-generated
    jusrisdiction = models.CharField(max_length=100)
    src_type = models.CharField(max_length=100)
    src_tblnm = models.CharField(max_length=100)
    tgt_tblnm = models.CharField(max_length=100)
    tgt_tblcols = models.CharField(max_length=100)
    mapng_nm = models.CharField(max_length=100)
    mpngtxt = models.CharField(max_length=100)
    insrt_TIMESTAMP = models.DateTimeField(auto_now_add=True)  # Assuming Insert_TIMESTAMP is auto-generated

    class Meta:
        managed = False  # Django won't manage this table as it's already created in the database
        db_table = 'ce_mapng'  # Specify the name of your existing table


class c_extr_tables(models.Model):
    SID = models.AutoField(primary_key=True)
    Jurisdiction = models.CharField(max_length=100)
    AcctSytesm = models.CharField(max_length=100)
    Src_Host = models.CharField(max_length=100)
    Src_DB_Name = models.CharField(max_length=100)
    Src_Port = models.CharField(max_length=100)
    Src_Tables = models.CharField(max_length=100, blank=False, null=False)
    Src_UPDATE_TIME = models.DateTimeField(default=timezone.now)
    src_type = models.CharField(max_length=100)

    class Meta:
        managed = False  # Django won't manage this table as it's already created in the database
        db_table = 'c_extr_tables'  # Specify the name of your existing table

class c_extr_table_cols(models.Model):
    SID = models.AutoField(primary_key=True)
    Jurisdiction = models.CharField(max_length=100)
    AcctSytesm = models.CharField(max_length=100)
    Src_Host = models.CharField(max_length=100)
    Src_DB_Name = models.CharField(max_length=100)
    Src_Port = models.CharField(max_length=100)
    Src_Table = models.CharField(max_length=100, blank=False, null=False) 
    Src_Columns = models.CharField(max_length=1000)
    Src_UPDATE_TIME = models.DateTimeField(default=timezone.now)
    src_type = models.CharField(max_length=100)

    class Meta:
        managed = False  # Django won't manage this table as it's already created in the database
        db_table = 'c_extr_table_cols'  # Specify the name of your existing table