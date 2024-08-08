from django.db import models

class CE_US_IC_Inventory_v(models.Model):
    id = models.AutoField(primary_key=True)

    Year = models.CharField(max_length=4, primary_key=False)
    month = models.CharField(max_length=10, primary_key=False)
    GLAccount = models.CharField(max_length=100, primary_key=False)
    Actual = models.DecimalField(max_digits=10, decimal_places=2, primary_key=False)
    Quantity = models.IntegerField(primary_key=False)
    sku = models.CharField(max_length=100, primary_key=False)

    class Meta:
        managed = False
        db_table = 'CE_US_IC_Inventory_v'

class USA_Guide(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_sheet = models.CharField(max_length=50)
    short_instruction = models.TextField()

    class Meta:
        managed = False
        db_table = 'USA_Guide'
        
class BAL_Guide(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_sheet = models.CharField(max_length=50)
    short_instruction = models.TextField()

    class Meta:
        managed = False
        db_table = 'BAL_Guide'
        
class AZRB_Guide(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_sheet = models.CharField(max_length=50)
    short_instruction = models.TextField()

    class Meta:
        managed = False
        db_table = 'AZRB_Guide'
        
class IDSBorjomi_Guide(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_sheet = models.CharField(max_length=50)
    short_instruction = models.TextField()

    class Meta:
        managed = False
        db_table = 'IDSBorjomi_Guide'
        
class KZ_Guide(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_sheet = models.CharField(max_length=50)
    short_instruction = models.TextField()

    class Meta:
        managed = False
        db_table = 'KZ_Guide'
        
class UZ_Guide(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_sheet = models.CharField(max_length=50)
    short_instruction = models.TextField()

    class Meta:
        managed = False
        db_table = 'UZ_Guide'
    
class CE_US_IC_Trial_Balance_v(models.Model):
    month = models.CharField(max_length=10)
    ledger_Account = models.CharField(max_length=100)
    val = models.DecimalField(max_digits=10, decimal_places=2)
    Corection = models.DecimalField(max_digits=10, decimal_places=2)
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    Mapping = models.CharField(max_length=100)
    fsline = models.CharField(max_length=100)
    GA_Group = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'CE_US_IC_Trial_Balance_v'

class CE_US_IC_cogs_cust_v(models.Model):
    month = models.IntegerField(max_length=10)
    credit = models.IntegerField(max_length=100)
    

    class Meta:
        managed = False
        db_table = 'CE_US_IC_cogs_cust_v'

        
 
class CE_US_INFO1(models.Model):
    SKU = models.CharField(max_length=1000)
    RevGL = models.CharField(max_length=1000)
    COGSGL = models.IntegerField()
    InvGL = models.IntegerField()
    BrandGroup = models.CharField(max_length=1000)
    Vol = models.DecimalField(max_digits=10, decimal_places=2)
  

    class Meta:
        managed = False
        db_table = 'CE_US_INFO1'



class CE_US_INFO2(models.Model):
    Code = models.IntegerField()
    Groups = models.CharField(max_length=1000)
    Item = models.CharField(max_length=1000)
    FS_line = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'CE_US_INFO2'

# date, cost_unit, value, item, fs_line
# 
class CE_US_IC_marketing_v(models.Model):
    month = models.IntegerField()
    cost_unit = models.IntegerField()
    value = models.IntegerField()
    item = models.CharField(max_length=1000)
    fs_line = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'CE_US_IC_marketing_v'

#   , , , , 
      
class CE_US_IC_AP_AR_Reclass_v(models.Model):
    reknr = models.IntegerField()
    GLDesc = models.CharField(max_length=1000)
    Account = models.CharField(max_length=1000)
    value = models.IntegerField()
    ReclassGL = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CE_US_IC_AP_AR_Reclass_v'

# , , , , 

class CE_US_IC_Purchases_v(models.Model):
    month = models.IntegerField()
    SKU = models.CharField(max_length=1000)
    bottles = models.IntegerField()
    Liters = models.DecimalField(max_digits=10, decimal_places=2)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'CE_US_IC_Purchases_v'

# , , , , , , , 
      
class CE_US_IC_Sales_v(models.Model):
    month= models.IntegerField()
    reknr = models.IntegerField()
    GLAccount = models.CharField(max_length=1000)
    Gross_Revenue = models.DecimalField(max_digits=10, decimal_places=2)
    Bottles = models.IntegerField()
    SKU = models.CharField(max_length=1000)
    Liters = models.DecimalField(max_digits=10, decimal_places=2)
    COGS = models.IntegerField()
    cogs_customs = models.DecimalField(max_digits=10, decimal_places=2)
    cogs_logistics = models.DecimalField(max_digits=10, decimal_places=2)
    Gross_discount = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        managed = False
        db_table = 'CE_US_IC_Sales_v'


class Bs2InvBalancePurchase(models.Model):
    sid = models.IntegerField()
    val = models.CharField(max_length=1000, blank=True)
    bottles = models.FloatField(blank=True)
    month = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'BS_2_inv_Balance_purchase'

class Bs3OtherAssetsLiabilitiesV(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    monyy = models.CharField(db_column='MonYY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    runningtotal = models.FloatField(db_column='RunningTotal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS_3_Other_assets_liabilities_V'

class Bs4LeaseRollForwardV(models.Model):
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subcategory = models.CharField(db_column='Subcategory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    monyy = models.CharField(db_column='MonYY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS_4_Lease_roll_forward_V'

class Bs6Capex1V(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS_6_CAPEX_1_V'

class Bs6Capex2V(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BS_6_CAPEX_2_V'

class CeUsFinCostView(models.Model):
    fin_cost_heads = models.CharField(db_column='Fin_cost_Heads', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monyy = models.CharField(db_column='MonYY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CE_US_Fin_Cost_View'

class CeUsIcApArReclassV(models.Model):
    reknr = models.IntegerField(blank=True, null=True)
    gldesc = models.CharField(db_column='GLDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=50, blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(blank=True, null=True)
    reclassgl = models.IntegerField(db_column='ReclassGL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CE_US_IC_AP_AR_Reclass_v'

class CeUsIcBs01(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    monyy = models.DateField(db_column='MonYY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(blank=True, null=True)
    runningtotal = models.FloatField(db_column='RunningTotal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CE_US_IC_BS_0_1'

class CeUsIcBs7TaxesHeadsV(models.Model):
    category = models.CharField(db_column='Category', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subcategory = models.CharField(db_column='SubCategory', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monyy = models.CharField(max_length=6, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CE_US_IC_BS_7_Taxes_heads_V'

class CeUsIcGnaBcV(models.Model):
    dpt_name = models.CharField(db_column='Dpt_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monyy = models.CharField(db_column='MonYY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CE_US_IC_GNA_BC_v'

class CeUsIcGnaConsultV(models.Model):
    dpt_name = models.CharField(db_column='Dpt_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monyy = models.DateField(db_column='MonYY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CE_US_IC_GNA_Consult_v'

class CeUsIcGnaMon(models.Model):
    expense_type = models.CharField(db_column='Expense_type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monyy = models.DateField(db_column='Monyy', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CE_US_IC_GNA_Mon'

class CeUsIcGnaOeV(models.Model):
    dpt_name = models.CharField(db_column='Dpt_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monyy = models.DateField(db_column='MonYY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CE_US_IC_GNA_OE_v'

class CeUsIcGnaSfV(models.Model):
    dpt_name = models.CharField(db_column='Dpt_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monyy = models.DateField(db_column='MonYY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CE_US_IC_GNA_SF_v'

class CeUsIcGnaTcV(models.Model):
    dpt_name = models.CharField(db_column='Dpt_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CE_US_IC_GNA_TC_v'

class CeUsIcGnaTiV(models.Model):
    dpt_name = models.CharField(db_column='Dpt_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monyy = models.DateField(db_column='MonYY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CE_US_IC_GNA_TI_v'

class CtUsPl0V12(models.Model):
    group = models.CharField(db_column='GROUP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cluster = models.CharField(db_column='Cluster', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entity = models.CharField(db_column='Entity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sid = models.IntegerField(blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    monyy = models.CharField(max_length=6, blank=True, null=True)
    cat = models.CharField(max_length=50, blank=True, null=True)
    sub_cat = models.CharField(db_column='Sub_cat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    val = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_US_PL_0_V1_2'

class CtUsPl11IcV1(models.Model):
    category = models.CharField(db_column='Category', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subcategory = models.CharField(db_column='SubCategory', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monyy = models.DateField(db_column='MonYY', blank=True, null=True)  # Field name made lowercase.
    comp = models.CharField(max_length=6, blank=True, null=True)
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CT_US_PL_11_IC_V1'

class CtUsPl1Quantity1V(models.Model):
    sid = models.IntegerField()
    val = models.CharField(max_length=1000, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    monyy = models.CharField(max_length=6, blank=True, null=True)
    bottles = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_US_PL_1_Quantity1_V'

class CtUsPl1Quantity2V(models.Model):
    entity = models.CharField(max_length=20, blank=True, null=True)
    sid = models.IntegerField(blank=True, null=True)
    val = models.CharField(max_length=1000, blank=True, null=True)
    btls = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_US_PL_1_Quantity2_V'

class CtUsPl2GrossDiscount1V(models.Model):
    sid = models.IntegerField()
    val = models.CharField(max_length=1000, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    monyy = models.CharField(max_length=6, blank=True, null=True)
    gross_discount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_US_PL_2_gross_Discount1_V'

class CtUsPl2GrossDiscount2V(models.Model):
    sid = models.IntegerField()
    val = models.CharField(max_length=1000, blank=True, null=True)
    comp = models.CharField(max_length=6)
    grossdis = models.FloatField(db_column='grossDis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CT_US_PL_2_gross_discount2_V'

class CtUsPl2GrossRevenue1V(models.Model):
    sid = models.IntegerField()
    val = models.CharField(max_length=1000, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    monyy = models.DateField(blank=True, null=True)
    gross_revenue = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_US_PL_2_gross_revenue1_V'

class CtUsPl2GrossRevenue2V(models.Model):
    sid = models.IntegerField()
    val = models.CharField(max_length=1000, blank=True, null=True)
    comp = models.CharField(max_length=6)
    btls = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_US_PL_2_gross_revenue2_V'

class CtUsPl3GrossDiscount1V(models.Model):
    sid = models.IntegerField()
    val = models.CharField(max_length=1000, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    monyy = models.DateField(blank=True, null=True)
    gross_discount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_US_PL_3_gross_discount1_V'

class CtUsPl3GrossDiscount2V(models.Model):
    sid = models.IntegerField()
    val = models.CharField(max_length=1000, blank=True, null=True)
    comp = models.CharField(max_length=6)
    grossdis = models.FloatField(db_column='grossDis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CT_US_PL_3_gross_discount2_V'

class CtUsPl4Cogs1V(models.Model):
    sid = models.IntegerField(blank=True, null=True)
    val = models.CharField(max_length=1000, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    monyy = models.DateField(blank=True, null=True)
    cogs = models.FloatField(db_column='COGS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CT_US_PL_4_COGS1_V'

class CtUsPl4Cogs2V(models.Model):
    sid = models.IntegerField(blank=True, null=True)
    comp = models.CharField(max_length=20, blank=True, null=True)
    fgid = models.IntegerField(blank=True, null=True)
    val = models.CharField(max_length=1000, blank=True, null=True)
    cogs = models.FloatField(db_column='COGS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CT_US_PL_4_COGS2_V'

class CtUsPl4CogsCustomV(models.Model):
    sid = models.IntegerField(blank=True, null=True)
    val = models.CharField(max_length=1000, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    monyy = models.DateField(blank=True, null=True)
    cogs_customs = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_US_PL_4_COGS_Custom_V'

class CtUsPl4CogsMonV(models.Model):
    sid = models.IntegerField(blank=True, null=True)
    val = models.CharField(max_length=1000, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    monyy = models.DateField(blank=True, null=True)
    cogs = models.FloatField(db_column='COGS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CT_US_PL_4_COGS_MON_V'

class CtUsPl4CogsLogisticsV(models.Model):
    sid = models.IntegerField(blank=True, null=True)
    val = models.CharField(max_length=1000, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    monyy = models.DateField(blank=True, null=True)
    cogs_logistics = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_US_PL_4_cogs_logistics_V'

class CtUsPl6Log1(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CT_US_PL_6_log_1'

class CtUsPl6Log2(models.Model):
    entity = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_US_PL_6_log_2'

class CtUsPnl9ForexV(models.Model):
    field_cost_heads = models.CharField(db_column='_cost_Heads', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    monyy = models.CharField(db_column='MonYY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CT_US_PnL_9_Forex_v'

class CtCwcPl0V12(models.Model):
    group = models.CharField(db_column='GROUP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cluster = models.CharField(db_column='Cluster', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entity = models.CharField(db_column='Entity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sid = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    monyy = models.CharField(max_length=6, blank=True, null=True)
    cat = models.CharField(max_length=50, blank=True, null=True)
    sub_cat = models.CharField(db_column='Sub_cat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    val = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CT_cwc_PL_0_V1_2'

class CtUsBs2InvBalanceDateAtV(models.Model):
    sid = models.IntegerField()
    val = models.CharField(max_length=1000, blank=True, null=True)
    insrt_timestamp = models.DateTimeField(db_column='insrt_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=100, blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(max_length=2, blank=True, null=True)
    glaccount = models.CharField(db_column='GLAccount', max_length=113, blank=True, null=True)  # Field name made lowercase.
    actual = models.FloatField(db_column='Actual', blank=True, null=True)  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    sku = models.CharField(max_length=50, blank=True, null=True)
    runningtotalquantity = models.FloatField(db_column='RunningTotalQuantity', blank=True, null=True)  # Field name made lowercase.
    runningtotalactual = models.FloatField(db_column='RunningTotalActual', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ct_US_BS_2_inv_Balance_date_at_v'

class CtUsBs2InvBalancePurchase(models.Model):
    sid = models.IntegerField()
    val = models.CharField(max_length=1000, blank=True, null=True)
    bottles = models.FloatField(blank=True, null=True)
    month = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ct_US_BS_2_inv_Balance_purchase'

class CtUsPnl0V(models.Model):
    sid = models.IntegerField(db_column='SID', blank=True, null=True)  # Field name made lowercase.
    cat = models.CharField(max_length=50, blank=True, null=True)
    sub_cat = models.CharField(db_column='Sub_cat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    monyy = models.CharField(max_length=6, blank=True, null=True)
    val = models.CharField(max_length= 225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ct_US_PnL_0_v'
