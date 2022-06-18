from django.urls import path
from .import views

urlpatterns = [
    path('',views.deposits,name='test1'),
    path('test2',views.test2,name='test2'),
    path('test3',views.test3,name='test3'),
    path('ledger',views.ledger,name='ledger'),
    path('load_create_ledgers',views.load_create_ledgers,name='load_create_ledgers'),
    path('load_bank_search',views.load_bank_search,name='load_bank_search'),
    path('load_ledger_search',views.load_ledger_search,name='load_ledger_search'),
    path('load_bankledger_search',views.load_bankledger_search,name='load_bankledger_search'),

]