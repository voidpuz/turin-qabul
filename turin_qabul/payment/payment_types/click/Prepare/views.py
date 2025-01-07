from django.db import transaction as db_transaction
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from payment.models import Transaction
from payment.payment_types.click.auth import authentication
from payment.payment_types.click.provider import ClickProvider
from payment.payment_types.click.views import PaymentView
from rest_framework.response import Response

from .serializers import ClickPrepareSerializer


class ClickPrepareAPIView(PaymentView):
    TYPE = "prepare"
    PROVIDER = Transaction.PaymentType.CLICK  # type: ignore
    permission_classes = []

    @extend_schema(
        request=ClickPrepareSerializer,
    )
    def post(self, request, *args, **kwargs):
        is_authenticated = authentication(request)
        if not is_authenticated:
            return Response({"error": "-1", "error_note": _("SIGN CHECK FAILED!")})
        serializer = ClickPrepareSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)

        with db_transaction.atomic():
            click_provider = ClickProvider(serializer.validated_data)
            response = click_provider.prepare()

        if click_provider.has_transaction:
            transaction = click_provider.transaction
        else:
            transaction = None

        response["click_trans_id"] = serializer.validated_data.get("click_trans_id", None)
        response["merchant_trans_id"] = serializer.validated_data.get("merchant_trans_id", None)

        if response["error"] == "0":
            transaction = click_provider.transaction
            response["merchant_prepare_id"] = transaction.id
            return Response(response)

        if transaction and transaction.status == Transaction.StatusType.PENDING:
            transaction.status = Transaction.StatusType.REJECTED
            transaction.save()

        return Response(response)


__all__ = ["ClickPrepareAPIView"]
