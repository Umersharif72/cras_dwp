# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Eje(models.Model):
    aje_number = models.IntegerField(db_column='AJE_Number', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    period = models.IntegerField(db_column='Period', blank=True, null=True)  # Field name made lowercase.
    cluster = models.CharField(db_column='Cluster', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dr_cr = models.CharField(db_column='DR_CR', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bs_pl = models.CharField(db_column='BS_PL', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    line = models.CharField(db_column='Line', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    decomposition1 = models.CharField(db_column='Decomposition1', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    decomposition2 = models.CharField(db_column='Decomposition2', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    amount_in_usd = models.DecimalField(db_column='Amount_in_USD', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EJE'
