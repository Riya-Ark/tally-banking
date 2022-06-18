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
     date=models.DateField()

class Particulars(models.Model):
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)
    amount=models.IntegerField()


class Payment(models.Model):
    no=models.IntegerField()   
    date=models.ForeignKey(account,on_delete=models.CASCADE,blank=False)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,blank=False)
    transactiontype=models.ForeignKey(transactiontype,on_delete=models.CASCADE,blank=False)
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)

class Receipt(models.Model):
    no=models.IntegerField()   
    date=models.ForeignKey(account,on_delete=models.CASCADE,blank=False)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,blank=False)
    transactiontype=models.ForeignKey(transactiontype,on_delete=models.CASCADE,blank=False)
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)

   

   


class Contra(models.Model):
    no=models.IntegerField()   
    # date=models.ForeignKey(account,on_delete=models.CASCADE,blank=False)
    amount=models.IntegerField(default=False)
    transactiontype=models.CharField(max_length=10)
    particualrs=models.CharField(max_length=100)


class sales(models.Model):
    no=models.IntegerField()   
    date=models.ForeignKey(account,on_delete=models.CASCADE,blank=False)
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,blank=False)
    transactiontype=models.ForeignKey(transactiontype,on_delete=models.CASCADE,blank=False)
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,blank=False)




    

