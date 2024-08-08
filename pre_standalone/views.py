from .models import *
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
import csv
from .filters import *


def generate_csv(request):
    if request.method == "POST":
        csv_data = request.POST.get("csv_data")
        file_name = request.POST.get("file_name")

        if not csv_data or not file_name:
            return HttpResponse(status=400)

        # Create the HttpResponse object with the appropriate CSV header
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="' + file_name + '"'

        writer = csv.writer(response)

        # Write the data to the CSV file
        rows = csv_data.split("\n")
        for row in rows:
            writer.writerow(row.split(","))

        return response

    return HttpResponse(status=405)  # Method Not Allowed


def usa_guide_list(request):
    guides = USA_Guide.objects.all()
    print(guides)
    return render(request, 'Main/landingpage.html', {'guides': guides})

def bal_guide_list(request):
    guides = BAL_Guide.objects.all()
    print(guides)
    return render(request, 'Main/BAL_g.html', {'bal_guides': guides})

def azrb_guide_list(request):
    guides = AZRB_Guide.objects.all()
    print(guides)
    return render(request, 'Main/landingpage.html', {'azrb_guides': guides})

def idsbjm_guide_list(request):
    guides =IDSBorjomi_Guide.objects.all()
    print(guides)
    return render(request, 'Main/IDSBJM_g.html', {'idsbjm_guides': guides})

def kz_guide_list(request):
    guides =KZ_Guide.objects.all()
    print(guides)
    return render(request, 'Main/landingpage.html', {'kz_guides': guides})

def uz_guide_list(request):
    guides =UZ_Guide.objects.all()
    print(guides)
    return render(request, 'Main/UZ_g.html', {'uz_guides': guides})

def fetch_inventory(request):
    records = CE_US_IC_Inventory_v.objects.values('Year', 'month', 'GLAccount', 'Actual', 'Quantity', 'sku')
    headings = [field for field in CE_US_IC_Inventory_v._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_Balance(request):
    records = CE_US_IC_Trial_Balance_v.objects.values('month', 'ledger_Account', 'val', 'Corection', 'Total', 'Mapping', 'fsline', 'GA_Group')
    headings = [field for field in CE_US_IC_Trial_Balance_v._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_COGS(request):
    records = CE_US_IC_cogs_cust_v.objects.values('month', 'credit')
    headings = [field for field in CE_US_IC_cogs_cust_v._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_INFO1(request):
    records = CE_US_INFO1.objects.values('SKU', 'RevGL', 'COGSGL', 'InvGL', 'BrandGroup', 'Vol')
    headings = [field for field in CE_US_INFO1._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_INFO2(request):
    records = CE_US_INFO2.objects.values('Code', 'Groups', 'Item', 'FS_line')
    headings = [field for field in CE_US_INFO2._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})


def fetch_marketing(request):
    records = CE_US_IC_marketing_v.objects.values('month', 'cost_unit', 'value', 'item', 'fs_line')
    headings = [field for field in CE_US_IC_marketing_v._meta.get_fields() if field.name != 'id']
    myfilter = DateFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})


def fetch_reclass(request):
    records = CE_US_IC_AP_AR_Reclass_v.objects.values('reknr', 'GLDesc', 'Account', 'value', 'ReclassGL')
    headings = [field for field in CE_US_IC_AP_AR_Reclass_v._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})


def fetch_sales(request):
    records = CE_US_IC_Sales_v.objects.values('month', 'reknr', 'GLAccount', 'Gross_Revenue', 'Bottles', 'SKU', 'Liters', 'COGS', 'cogs_customs', 'cogs_logistics', 'Gross_discount')
    headings = [field for field in CE_US_IC_Sales_v._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})


def fetch_purchases(request):
    records = CE_US_IC_Purchases_v.objects.values('month', 'SKU', 'bottles', 'Liters', 'Amount')
    headings = [field for field in CE_US_IC_Purchases_v._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})


def fetch_invbalancepurchase(request):
    records = Bs2InvBalancePurchase.objects.values('val', 'bottles', 'month')
    headings = [field for field in Bs2InvBalancePurchase._meta.get_fields() if field.name not in ['id', 'sid']]

    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_otherassetliabilities(request):
    records = Bs3OtherAssetsLiabilitiesV.objects.values('category', 'subcategory', 'monyy', 'runningtotal')
    headings = [field for field in Bs3OtherAssetsLiabilitiesV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_leaserollforward(request):
    records = Bs4LeaseRollForwardV.objects.values('category', 'subcategory', 'total', 'monyy', 'date2')
    headings = [field for field in Bs4LeaseRollForwardV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_capex1v(request):
    records = Bs6Capex1V.objects.values('category', 'month', 'date2')
    headings = [field for field in Bs6Capex1V._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_capex2v(request):
    records = Bs6Capex2V.objects.values('category', 'month', 'date2')
    headings = [field for field in Bs6Capex2V._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_fincostview(request):
    records = CeUsFinCostView.objects.values('fin_cost_heads', 'monyy', 'total')
    headings = [field for field in CeUsFinCostView._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_01(request):
    records = CeUsIcBs01.objects.values('category', 'subcategory', 'monyy', 'total', 'month', 'runningtotal')
    headings = [field for field in CeUsIcBs01._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_taxeshead(request):
    records = CeUsIcBs7TaxesHeadsV.objects.values('category', 'subcategory', 'monyy', 'month', 'date2', 'total')
    headings = [field for field in CeUsIcBs7TaxesHeadsV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_bcv(request):
    records = CeUsIcGnaBcV.objects.values('dpt_name', 'monyy', 'total')
    headings = [field for field in CeUsIcGnaBcV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_consult(request):
    records = CeUsIcGnaConsultV.objects.values('dpt_name', 'monyy', 'total')
    headings = [field for field in CeUsIcGnaConsultV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_mon(request):
    records = CeUsIcGnaMon.objects.values('expense_type', 'monyy', 'total')
    headings = [field for field in CeUsIcGnaMon._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_0ev(request):
    records = CeUsIcGnaOeV.objects.values('dpt_name', 'monyy', 'total')
    headings = [field for field in CeUsIcGnaOeV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_sfv(request):
    records = CeUsIcGnaSfV.objects.values('dpt_name', 'monyy', 'total')
    headings = [field for field in CeUsIcGnaSfV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_tcv(request):
    records = CeUsIcGnaTcV.objects.values('dpt_name', 'month', 'total')
    headings = [field for field in CeUsIcGnaTcV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_tiv(request):
    records = CeUsIcGnaTiV.objects.values('dpt_name', 'monyy', 'total')
    headings = [field for field in CeUsIcGnaTiV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})


def fetch_l0V12(request):
    records = CtUsPl0V12.objects.values('group', 'cluster', 'entity', 'month', 'date2', 'monyy', 'cat', 'sub_cat', 'val')
    headings = [field for field in CtUsPl0V12._meta.get_fields() if field.name not in ['id', 'sid', 'cid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_11IcV1(request):
    records = CtUsPl11IcV1.objects.values('category', 'subcategory', 'monyy', 'comp', 'total')
    headings = [field for field in CtUsPl11IcV1._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_quantity1v(request):
    records = CtUsPl1Quantity1V.objects.values('val', 'month', 'monyy', 'bottles')
    headings = [field for field in CtUsPl1Quantity1V._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_quantity2v(request):
    records = CtUsPl1Quantity2V.objects.values('entity', 'val', 'btls')
    headings = [field for field in CtUsPl1Quantity2V._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_grossdiscount1v(request):
    records = CtUsPl2GrossDiscount1V.objects.values('val', 'month', 'monyy', 'gross_discount')
    headings = [field for field in CtUsPl2GrossDiscount1V._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_grossdiscount2v(request):
    records = CtUsPl2GrossDiscount2V.objects.values('val', 'comp', 'grossdis')
    headings = [field for field in CtUsPl2GrossDiscount2V._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_grossrevenue1v(request):
    records = CtUsPl2GrossRevenue1V.objects.values('val', 'month', 'monyy', 'gross_revenue')
    headings = [field for field in CtUsPl2GrossRevenue1V._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_grossrevenue2v(request):
    records = CtUsPl2GrossRevenue2V.objects.values('val', 'comp', 'btls')
    headings = [field for field in CtUsPl2GrossRevenue2V._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_cogs1v(request):
    records = CtUsPl4Cogs1V.objects.values('val', 'month', 'monyy', 'cogs')
    headings = [field for field in CtUsPl4Cogs1V._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_cogs2v(request):
    records = CtUsPl4Cogs2V.objects.values('comp', 'fgid', 'val', 'cogs')
    headings = [field for field in CtUsPl4Cogs2V._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_cogscustom(request):
    records = CtUsPl4CogsCustomV.objects.values('val', 'month', 'monyy', 'cogs_customs')
    headings = [field for field in CtUsPl4CogsCustomV._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_cogsmon(request):
    records = CtUsPl4CogsMonV.objects.values('val', 'month', 'monyy', 'cogs')
    headings = [field for field in CtUsPl4CogsMonV._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_coglog(request):
    records = CtUsPl4CogsLogisticsV.objects.values('val', 'month', 'monyy', 'cogs_logistics')
    headings = [field for field in CtUsPl4CogsLogisticsV._meta.get_fields() if field.name not in ['id', 'sid']]
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_log1(request):
    records = CtUsPl6Log1.objects.values('category', 'month', 'date2', 'total')
    headings = [field for field in CtUsPl6Log1._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_ct_us_pl_6_log_2(request):
    records = CtUsPl6Log2.objects.values('entity', 'category', 'total')
    headings = [field for field in CtUsPl6Log2._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_ct_us_pnl_9_forex_v(request):
    records = CtUsPnl9ForexV.objects.values('field_cost_heads', 'monyy', 'total')
    headings = [field for field in CtUsPnl9ForexV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_ct_cwc_pl_0_v12(request):
    records = CtCwcPl0V12.objects.values('group', 'cluster', 'entity', 'sid', 'month', 'date2', 'monyy', 'cat', 'sub_cat', 'val')
    headings = [field for field in CtCwcPl0V12._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_ct_us_bs_2_inv_balance_date_at_v(request):
    records = CtUsBs2InvBalanceDateAtV.objects.values('sid', 'val', 'insrt_timestamp', 'year', 'month', 'glaccount', 'actual', 'quantity', 'sku', 'runningtotalquantity', 'runningtotalactual')
    headings = [field for field in CtUsBs2InvBalanceDateAtV._meta.get_fields() if field.name != 'id']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_ct_us_bs_2_inv_balance_purchase(request):
    records = CtUsBs2InvBalancePurchase.objects.values('val', 'bottles', 'month')
    headings = [field for field in CtUsBs2InvBalancePurchase._meta.get_fields() if field.name != 'id' and field.name != 'sid']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})

def fetch_ct_us_pnl_0_v(request):
    records = CtUsPnl0V.objects.values('cat', 'sub_cat', 'month', 'monyy', 'val')
    headings = [field for field in CtUsPnl0V._meta.get_fields() if field.name != 'id' and field.name != 'sid']
    myfilter = CalenderFilter(request.GET, queryset=records)
    records = myfilter.qs
    return render(request, 'Main/landingpage.html', {'records': records, 'headings': headings, 'filter':myfilter})
