from django.db import models

# Create your models here.
from pyexpat import model
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


class contra(models.Model):
    account=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)
    Particulars=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)
    amount=models.IntegerField()
    transactiontype=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)


        
    def _str_(self):
     return self.account

class receipt(models.Model):
    account=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)
    Particulars=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)
    amount=models.IntegerField()
    transactiontype=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)
     
    