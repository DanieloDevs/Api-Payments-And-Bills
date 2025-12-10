from rest_framework import routers
from .views import BankAccountViewSet, BillViewSet, PaymentViewSet, TransactionHistoryViewSet

router = routers.DefaultRouter()
router.register(r'accounts', BankAccountViewSet)
router.register(r'bills', BillViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'transactions', TransactionHistoryViewSet)

urlpatterns = router.urls