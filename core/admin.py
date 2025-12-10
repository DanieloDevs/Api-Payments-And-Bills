from django.contrib import admin
from .models import BankAccount, Bill, Payment, TransactionHistory


admin.site.register(BankAccount)
admin.site.register(Bill)
admin.site.register(Payment)
admin.site.register(TransactionHistory)