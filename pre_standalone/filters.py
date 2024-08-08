import django_filters

from .models import *


class DateFilter(django_filters.FilterSet):

    class Meta:
        model = CE_US_IC_marketing_v
        fields = ['month']



class CalenderFilter(django_filters.FilterSet):

    class Meta:
        model = CeUsIcGnaTcV
        fields = ['month']

    class Meta:
        model = CE_US_IC_Sales_v
        fields = ['month']

    class Meta:
        model = CE_US_IC_Inventory_v
        fields = ['month']

    class Meta:
        model = CE_US_IC_Trial_Balance_v
        fields = ['month']
    
    class Meta:
        model = CE_US_IC_cogs_cust_v
        fields = ['month']

    class Meta:
        model = CE_US_IC_Sales_v
        fields = ['month']
    
    class Meta:
        model = CE_US_IC_Purchases_v
        fields = ['month']
    
    class Meta:
        model = Bs2InvBalancePurchase
        fields = ['month']

    class Meta:
        model = Bs6Capex1V
        fields = ['month']
    
    class Meta:
        model = Bs6Capex2V
        fields = ['month']
    
    class Meta:
        model = CeUsIcBs01
        fields = ['month']

    class Meta:
        model = CeUsIcBs7TaxesHeadsV
        fields = ['month']

    class Meta:
        model = CtUsPl0V12
        fields = ['month']
    
    class Meta:
        model = CtUsPl1Quantity1V
        fields = ['month']
    
    class Meta:
        model = CtUsPl2GrossDiscount1V
        fields = ['month']

    class Meta:
        model = CtUsPl2GrossRevenue1V
        fields = ['month']
    
    class Meta:
        model = CtUsPl4Cogs1V
        fields = ['month']
    
    class Meta:
        model = CtUsPl4CogsCustomV
        fields = ['month']

    class Meta:
        model = CtUsPl4CogsMonV
        fields = ['month']
    
    class Meta:
        model = CtUsPl4CogsLogisticsV
        fields = ['month']
    
    class Meta:
        model = CtUsPl6Log1
        fields = ['month']

    class Meta:
        model = CtCwcPl0V12
        fields = ['month']

    class Meta:
        model = CtUsBs2InvBalanceDateAtV
        fields = ['month']
    
    class Meta:
        model = CtUsBs2InvBalancePurchase
        fields = ['month']
    
    class Meta:
        model = CtUsPnl0V
        fields = ['month']

    