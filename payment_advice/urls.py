from django.urls import path
from .import views

urlpatterns = [

    # path('',views.test3,name='test3'),
    path('advice_view',views.advice_view,name='advice_view'),
    path('depos',views.depos,name='depos'),

    path('deposits',views.deposits,name='test1'),
    path('test2',views.test2,name='test2'),
    path('test3',views.test3,name='test3'),
    path('ledger',views.ledger,name='ledger'),
    path('load_create_ledgers',views.load_create_ledgers,name='load_create_ledgers'),
    path('load_bank_search',views.load_bank_search,name='load_bank_search'),
    path('load_ledger_search',views.load_ledger_search,name='load_ledger_search'),
    path('load_bankledger_search',views.load_bankledger_search,name='load_bankledger_search'),
    path('reconciliation',views.reconciliation,name='reconciliation'),
    path('reconciliation1',views.reconciliation1,name='reconciliation1'),
    path('reconciliation2',views.reconciliation2,name='reconciliation2'),
    path('reconciliation3',views.reconciliation3,name='reconciliation3'),
    
    path('credit_amount',views.credit_amount,name='credit_amount'),

]