from contextlib import nullcontext
from django.shortcuts import render, redirect
from .models import *

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
    results=Bank_name.objects.all
    return render(request,'load_bank_search.html',{'showbank':results})

def load_ledger_search(request):
    results=ledger_name.objects.all
    return render(request,'load_ledger_search.html',{'showledger':results})

    
def load_bankledger_search(request):
    return render(request,'load_bankledger_search.html')



# deposit slip
def deposits(request):
    deposit = Contra.objects.filter(particualrs='cash').values()
    context = {'my_list': deposit}
    return render(request, 'test1.html', context)

def depos(request):
    depo = Receipt.objects.filter(particualrs='Cheque')
    context={'rlist': depo}

    return render(request,'test1.html',context)

def depo(request):
    dep=payment_voucher.objects.filter(account='sbi').values()
    context={'li':dep}
    return render(request,'test1.html',context)


def advice_view(request):

    payment_slip = payment_voucher.objects.all()
    context = {'payment': payment_slip}
    return render(request, 'test3.html', context)

