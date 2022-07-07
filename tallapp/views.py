from django.urls import path
from .import views
import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import  *
from django.db.models import Count
from django.contrib import messages
import datetime
import fiscalyear
from fiscalyear import *
from dateutil import relativedelta


# Create your views here.
def home(request):
    return render(request,'base.html')
def searchbank(request):
    group=groups.objects.get(group="bank account")
    

    led=ledger.objects.filter(group=group.id)
    

    return render(request,'search_bank.html',{'l':led})

def deposit(request,id):
    led=ledger.objects.get(id=id)
    uid=led.id
    
    v=Vouchertype.objects.all()
    for v in v:
        if v.vouchertype=='payment':
            vid=v.id


   
    bak=bank.objects.filter(~Q(vouchertype=vid)).filter(ledger=uid)
    return render(request,'deposit_slip.html',{'bank':bak,'vi':v})


def searchledger(request):
    group=groups.objects.get(group= "ledger account")
    led=ledger.objects.filter(group=group.id)
    return render(request,'search_ledger.html',{'l':led})

def payment_advice(request,id):
    led=ledger.objects.get(id=id)
    uid=led.id
    
    v=Vouchertype.objects.all()
    for v in v:
        if v.vouchertype=='payment':
            vid=v.id


   
    bak=bank.objects.filter(vouchertype=vid).filter(ledger=uid)
    return render(request,'payment_advice.html',{'bank':bak,'vi':v})
def searchbank1(request):
    group=groups.objects.get(group="bank account")
    

    led=ledger.objects.filter(group=group.id)
    

    return render(request,'search_bank1.html',{'l':led})



def reconciliation(request,id):
    bk=bank.object.filter(ledger=id)
    credit={}
    debit={}
    con=contra.objects.all()
    pay=payment.objects.all()
    rec=receipt.objects.all()
    
    

#     check_payment = payment.objects.all()
#     context={'pay':check_payment}
#     return render(request,'bank_reconcilliation.html',context)
# def reconciliation1(request):
#     check_contra=contra.objects.all()
#     context={'contra':check_contra}
#     return render(request,'bank_reconcilliation.html',context)
# def reconciliation3(request):
#     check_sales=sales.objects.all()
#     context={'sales':check_sales}
#     return render(request,'bank_reconcilliation.html',context)
# def reconciliation4(request):
#     check_journal=journal.objects.all()
#     context={'journal':check_journal}
#     return render(request,'bank_reconcilliation.html',context)
# def reconciliation5(request):
#     check_receipt=receipt.objects.all()
#     context={'sales':check_receipt}
#     return render(request,'bank_reconcilliation.html',context)







