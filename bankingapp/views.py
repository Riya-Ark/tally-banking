from django.shortcuts import render
from bankingapp.models import *

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
    return render(request,'load_bank_search.html')
def load_ledger_search(request):
    return render(request,'load_ledger_search.html')
def load_bankledger_search(request):
    return render(request,'load_bankledger_search.html')


def deposits(request):
    deposit = Contra.objects.filter(particualrs='cash')
    context = {'deposit': deposit}
    return render(request, 'test1.html', context)