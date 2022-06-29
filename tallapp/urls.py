from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('searchbank',views.searchbank,name='searchbank'),
    path('deposit/<int:id>',views.deposit,name='deposit'),

]