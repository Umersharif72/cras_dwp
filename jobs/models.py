from django.db import models

# Create your models here.
class CeMapng(models.Model):
    sid = models.AutoField(db_column='SID', primary_key=True)  # Field name made lowercase.
    jusrisdiction = models.CharField(db_column='Jusrisdiction', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    src_type = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    src_tblnm = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tgt_tblnm = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tgt_tblcols = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # This field type is a guess.
    mapng_nm = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    mpngtxt = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # This field type is a guess.
    insrt_timestamp = models.DateTimeField(db_column='insrt_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ce_mapng'