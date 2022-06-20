from django.db import models
# Create your models here.


class groups(models.Model):
    group=models.CharField(max_length=225)


    def _str_(self):
     return self.group

class ledger(models.Model):
    group=models.ForeignKey(groups,on_delete=models.CASCADE,blank=False)
    name=models.CharField(max_length=225)
    
    def _str_(self):
     return self.name
class transactiontype(models.Model):
    transactiontype=models.CharField(max_length=225)

class account(models.Model):
     
     account=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)
    #  date=models.DateField()

class Particulars(models.Model):
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)
    amount=models.IntegerField()

class Bank_name(models.Model):
    name=models.CharField(max_length=25)
    
    def _str_(self):
         return self.name

class ledger_name(models.Model):
    ledger=models.CharField(max_length=25)
    
    def _str_(self):
         return self.ledger

class Payment(models.Model):
    no=models.IntegerField() 
    amount=models.IntegerField(default=False)
    transactiontype=models.CharField(max_length=10)
    particualrs=models.CharField(max_length=100) 
    # instrument_no=models.IntegerField(default=False) 
    # instrument_date=models.DateField(default=False) 
    def _str_(self):
         return self
    
    
class Receipt(models.Model):
    no=models.IntegerField()   
    # date=models.ForeignKey(account,on_delete=models.CASCADE,blank=False)
    amount=models.IntegerField(default=False)
    transactiontype=models.CharField(max_length=10)
    particualrs=models.CharField(max_length=100)
    instrument_no=models.IntegerField(default=False) 
    # instrument_date=models.DateField(default=False) 
    def _str_(self):
         return self
    

   


class Contra(models.Model):
    no=models.IntegerField()   
    # date=models.ForeignKey(account,on_delete=models.CASCADE,blank=False)
    amount=models.IntegerField(default=False)
    transactiontype=models.CharField(max_length=10)
    particualrs=models.CharField(max_length=100)
    # instrument_no=models.IntegerField(default=False) 
    # instrument_date=models.DateField() 
    def _str_(self):
         return self
    

class sales(models.Model):
    no=models.IntegerField()   
    # date=models.ForeignKey(account,on_delete=models.CASCADE,blank=False)
    amount=models.IntegerField(default=False)
    transactiontype=models.CharField(max_length=10)
    particualrs=models.CharField(max_length=100)
    # instrument_no=models.IntegerField(default=False) 
    # instrument_date=models.DateField(default=False) 
    def _str_(self):
         return self
    



    

