from django.contrib import admin

from .models import ledgers, payment_voucher,Contra,Receipt,sales
# Register your models here.

admin.site.register(ledgers)
admin.site.register(payment_voucher)
admin.site.register(Contra)
admin.site.register(Receipt)
admin.site.register(sales)