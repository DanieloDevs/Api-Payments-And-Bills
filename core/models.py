from django.db import models

from django.db import models
from django.utils import timezone

class BankAccount(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} ({self.account_number})"


class Bill(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_CANCELLED = 'cancelled'
    STATUS_PAID = 'paid'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_PAID, 'Paid'),
    ]

    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    creation_date = models.DateTimeField(default=timezone.now)
    approval_date = models.DateTimeField(blank=True, null=True)
    cancellation_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Bill {self.id} - {self.description} ({self.status})"


class Payment(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_CANCELLED = 'cancelled'
    STATUS_PAID = 'paid'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_PAID, 'Paid'),
    ]

    bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    account = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name='payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    creation_date = models.DateTimeField(default=timezone.now)
    approval_date = models.DateTimeField(blank=True, null=True)
    cancellation_date = models.DateTimeField(blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Payment {self.id} - {self.amount} ({self.status})"


class TransactionHistory(models.Model):
    TYPE_CHARGE = 'charge'
    TYPE_PAYMENT = 'payment'
    TYPE_CHOICES = [
        (TYPE_CHARGE, 'Charge'),
        (TYPE_PAYMENT, 'Payment'),
    ]

    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transactions')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date = models.DateTimeField(default=timezone.now)
    # optional: description or metadata
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Txn {self.id} - {self.type} - {self.amount}"
