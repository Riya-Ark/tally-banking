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
        if v.vouchertype=='Payment':
            vid=v.id


   
    bak=bank.objects.filter(~Q(vouchertype=vid)),filter(ledger=uid)
    return render(request,'deposit_slip.html',{'bank':bak,'vi':v})

def deposit_slip(request):
    
    dep=contra.objects.filter().values()
    context={'li':dep}
    return render(request,'deposit_slip.html',context)

def searchledger(request):
    group=groups.objects.get(group= "ledger account")
    led=ledger.objects.filter(group=group.id)
    return render(request,'search_ledger.html',{'l':led})

def payment_advice(request):
    payment_slip = payment.objects.filter()
    context = {'payment': payment_slip}
    return render(request,'payment_advice.html',context)

def reconciliation(request):
    check_payment = payment.objects.all()
    context={'pay':check_payment}
    return render(request,'bank_reconcilliation.html',context)



