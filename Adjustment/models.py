from django.db import models

# Create your models here.

class EJE(models.Model):
    AJE_Number = models.IntegerField(db_column='AJE_Number', blank=True, null=True)  # Field name made lowercase.
    Description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    Year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
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

class EntityAdjustment(models.Model):
    group = models.CharField(max_length=255, null=True, blank=True)
    cluster = models.CharField(max_length=255, null=True, blank=True)
    entity = models.CharField(max_length=255, null=True, blank=True)
    CompanyType= models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        managed = False
        db_table = 'EntityAdjustments'