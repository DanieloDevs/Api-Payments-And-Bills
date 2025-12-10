from rest_framework import serializers
from .models import BankAccount, Bill, Payment, TransactionHistory
from django.utils import timezone

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
        read_only_fields = ('creation_date',)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('creation_date',)

    def validate(self, data):
        # Simple validation: amount positive
        if data.get('amount') is None or data['amount'] <= 0:
            raise serializers.ValidationError("El monto de pago debe ser mayor a 0.")
        return data

    def create(self, validated_data):
        from .models import TransactionHistory
        account = validated_data['account']
        amount = validated_data['amount']


        p = Payment.objects.create(**validated_data)
        account.balance = account.balance - amount
        account.save()

        TransactionHistory.objects.create(
            account=account,
            payment=p,
            amount=amount,
            type=TransactionHistory.TYPE_PAYMENT,
            description=f"Pago ID {p.id} para Bill {p.bill_id if p.bill_id else 'N/A'}"
        )
        if p.bill:
            p.bill.status = Bill.STATUS_PAID
            p.bill.save()
        return p


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = '__all__'
        read_only_fields = ('date',)