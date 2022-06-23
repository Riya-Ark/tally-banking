from contextlib import nullcontext
from email.policy import default
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# Create your views here.

def test1(request):
    return render(request,'test1.html')
def test2(request):
    return render(request,'test2.html')
def test3(request):
    return render(request,'test3.html')
def ledger(request):
    return render(request, 'ledger.html')
def load_create_ledgers(request):
    return render(request,'load_create_ledgers.html')

def load_bank_search(request):
    results=ledgers.objects.all()
    return render(request,'load_bank_search.html',{'showbank':results})

def load_ledger_search(request):
    results=ledgers.objects.all
    return render(request,'load_ledger_search.html',{'showledger':results})

    
def load_bankledger_search(request):
    return render(request,'load_bankledger_search.html')



# deposit slipe
def deposits(request):
    results=request.POST.get("banks", False)
    return render(request, 'test1.html',{"banks":results})
    # deposit = Contra.objects.filter(particualrs='cash').values()
    # context = {'my_list': deposit}
    # return render(request, 'test1.html', context)

def depos(request):


    var = "sc"
    depo = Receipt.objects.filter(bank_names__group_list=var)
    context={'rlist': depo}

    return render(request,'test1.html',context)

def depo(request):
    dep=payment_voucher.objects.filter(account='sbi').values()
    context={'li':dep}
    return render(request,'test1.html',context)

def dep(request):
    dep=Journal.objects.filter(account='sbi').values
    context={'jlist':dep}
    return render(request,'test1.html',context)



def advice_view(request):

    payment_slip = payment_voucher.objects.filter(particulars__group_list = 'ELECTRICITY_BILL')
    context = {'payment': payment_slip}
    return render(request, 'test2.html', context)

def reconciliation(request):
    payment_v=payment_voucher.objects.all()
    context={'payment':payment_v}
    return render(request,'test3.html',context)

def reconciliation1(request):
    contra_v=Contra.objects.all()
    context1={'contra':contra_v}
    return render(request,'test3.html',context1)

def reconciliation2(request):
    sales_v=sales.objects.all()
    context2={'sale':sales_v}
    return render(request,'test3.html',context2)
    
def reconciliation3(request):
    receipt_v=Receipt.objects.all()
    context3={'receipt':receipt_v}
    return render(request,'test3.html',context3)


def credit_amount(request):
    check_payment = payment_voucher.objects.all()
    check_receipt = Receipt.objects.all()
    check_sales = sales.objects.all()
    check_contra = Contra.objects.all()
    check_journal = Journal.objects.all()

    return render(request, 'test3.html', {
        "check_payment": check_payment,
        "check_receipt": check_receipt,
        "check_sales": check_sales,
        "check_contra": check_contra,
        "check_journal": check_journal,
        } )








