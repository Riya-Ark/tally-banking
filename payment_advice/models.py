from tkinter import CASCADE
from django.db import models

# Create your models here.
class ledgers(models.Model):
    group_list = models.CharField(max_length=100)

    def __str__(self):
        return self.group_list

class voucher_type(models.Model):
    voucher=models.CharField(max_length=100)
    
    def __str__(self):
        return self.voucher



class payment_voucher(models.Model):
    pvoucher_no = models.AutoField(primary_key=True)
    pamount = models.IntegerField()
    transaction_type = models.ForeignKey(ledgers,on_delete=models.CASCADE, blank=False, related_name='transaction_type')
    bank_names = models.ForeignKey(ledgers, related_name='bank_names' ,on_delete=models.CASCADE, blank=False)
    particulars = models.ForeignKey(ledgers,related_name='particulars', on_delete=models.CASCADE, blank=False)

class Receipt(models.Model):
    no=models.IntegerField()   
    date=models.DateField()
    amount=models.IntegerField()
    bank_names = models.ForeignKey(ledgers, related_name='bank_name_receipt' ,on_delete=models.CASCADE, blank=False)
    transactiontype=models.CharField(max_length=10)
    particualrs=models.CharField(max_length=100)
    instrument_no=models.IntegerField() 
    instrument_date=models.DateField() 
    # def _str_(self):
    #      return self.bank_names
    
class Journal(models.Model):
    no=models.IntegerField()   
    date=models.DateField()
    amount=models.IntegerField()
    bank_names = models.ForeignKey(ledgers, related_name='bank_name_journal' ,on_delete=models.CASCADE, blank=False)
    transactiontype=models.CharField(max_length=10)
    particualrs=models.CharField(max_length=100)
    instrument_no=models.IntegerField() 
    instrument_date=models.DateField()

   


class Contra(models.Model):
    no=models.IntegerField()   
    date=models.DateField()
    amount=models.IntegerField()
    bank_names = models.ForeignKey(ledgers, related_name='bank_name_contra' ,on_delete=models.CASCADE, blank=False)
    transactiontype=models.CharField(max_length=10)
    particualrs=models.CharField(max_length=100)
    instrument_no=models.IntegerField() 
    instrument_date=models.DateField() 
    
    # def _str_(self):
    #      return self
    

class sales(models.Model):
    no=models.IntegerField()   
    date=models.DateField()
    amount=models.IntegerField()
    bank_names = models.ForeignKey(ledgers, related_name='bank_name_sales' ,on_delete=models.CASCADE, blank=False)
    transactiontype=models.CharField(max_length=10)
    particualrs=models.CharField(max_length=100)
    instrument_no=models.IntegerField() 
    instrument_date=models.DateField()  
    # def _str_(self):
    #      return self.
    


   

