from django.db import transaction
from rest_framework.views import APIView


class PaymentView(APIView):
    TYPE: str = ""
    PROVIDER: str = ""
    permission_classes = []

    @transaction.non_atomic_requests
    def dispatch(self, request, *args, **kwargs):
        # Logging for payment requests moved to middleware
        return super().dispatch(request, *args, **kwargs)
