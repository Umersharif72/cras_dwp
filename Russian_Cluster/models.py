from django.db import models

class Record(models.Model):
    entity = models.CharField(max_length=100)
    period = models.DateField()
    line_l1 = models.CharField(max_length=100)
    line_l2 = models.CharField(max_length=100)
    line_l3 = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    dlm = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.entity} - {self.period}"
    
    class Meta:
        managed = False
        # app_label = 'ru_standalone'
        db_table = 'PnLByEntity'
        


class CeUsIcGnaMon(models.Model):
    expense_type = models.CharField(db_column='Expense_type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monyy = models.DateField(db_column='Monyy', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CE_US_IC_GNA_Mon'
        app_label = 'ru_standalone'