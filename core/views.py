from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets, filters
from .models import BankAccount, Bill, Payment, TransactionHistory
from .serializers import BankAccountSerializer, BillSerializer, PaymentSerializer, TransactionHistorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'account_number', 'bank']

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description', 'status']

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        bill = self.get_object()
        bill.status = Bill.STATUS_APPROVED
        bill.approval_date = timezone.now()
        bill.save()
        return Response(BillSerializer(bill).data)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        bill = self.get_object()
        bill.status = Bill.STATUS_CANCELLED
        bill.cancellation_date = timezone.now()
        bill.save()
        return Response(BillSerializer(bill).data)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

class TransactionHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TransactionHistory.objects.all().order_by('-date')
    serializer_class = TransactionHistorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['type', 'description']