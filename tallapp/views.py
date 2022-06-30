from django.urls import path
from .import views
import datetime

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
    sum=0
    led=ledger.objects.get(id=id)
    uid=led.id
    bak=bank.objects.filter(ledger=uid)
    back=bak
    for  back in back:
        b=back.amount.amount
        sum=sum+b
    return render(request,'deposit_slip.html',{'bank':bak,'sum':sum})

def depo(request):
    
    dep=contra.objects.filter(account__group="bank account").values()
    context={'li':dep}
    return render(request,'deposit_slip.html',context)

def searchledger(request):
    group=groups.objects.get(group= "ledger account")
    led=ledger.objects.filter(group=group.id)
    return render(request,'search_ledger.html',{'l':led})

def payment_advice(request,id):
    return render(request,'payment_advice.html')

def reconciliation(request):
    return render(request,'bank_reconcilliation.html')


