import base64

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Transaction(models.Model):
    class StatusType(models.TextChoices):
        PENDING = "pending", _("Pending")
        ACCEPTED = "accepted", _("Accepted")
        REJECTED = "rejected", _("Rejected")
        CANCELED = "canceled", _("Canceled")

    class PaymentType(models.TextChoices):
        CLICK = "CLICK", _("CLICK")
        PAYME = "PAYME", _("PAYME")

    user = models.ForeignKey("admission.Admission", on_delete=models.PROTECT, related_name="transactions")
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2)
    status = models.CharField(_("Status"), max_length=32, choices=StatusType.choices, default=StatusType.PENDING)
    # tax_amount = models.DecimalField(_('TAX Amount'), max_digits=10, decimal_places=2, default=0.0, null=True,
    #                                  blank=True)
    paid_at = models.DateTimeField(verbose_name=_("Paid at"), null=True, blank=True)
    canceled_at = models.DateTimeField(verbose_name=_("Canceled at"), null=True, blank=True)
    payment_type = models.CharField(_("Payment Type"), choices=PaymentType.choices)
    commission = models.PositiveSmallIntegerField(verbose_name=_("Commission Percent"), default=0, db_default=0)
    fiscal_check_url = models.URLField(verbose_name=_("Fiscal check url"), null=True, blank=True)
    extra = models.JSONField(_("Extra"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    objects = models.Manager()

    class Meta:
        db_table = "Transaction"
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    def __str__(self):
        return f"{self.payment_type} | {self.id}"

    def success_process(self):
        self.status = self.StatusType.ACCEPTED
        self.paid_at = timezone.now()
        self.save(update_fields=["status", "paid_at"])

        self.user.update_balance()

    def cancel_process(self):
        self.status = self.StatusType.CANCELED
        self.canceled_at = timezone.now()
        self.save(update_fields=["status", "canceled_at"])

        self.user.update_balance()

    @property
    def payment_url(self):
        payment_url = ""
        if self.payment_type == Transaction.PaymentType.PAYME:
            merchant_id = settings.PAYMENT_CREDENTIALS["payme"]["merchant_id"]
            params = f"m={merchant_id};ac.order_id={self.id};a={self.amount * 100};"
            encode_params = base64.b64encode(params.encode("utf-8"))
            encode_params = str(encode_params, "utf-8")
            payment_url = f"{settings.PAYMENT_CREDENTIALS['payme']['callback_url']}/{encode_params}"

        elif self.payment_type == Transaction.PaymentType.CLICK:
            merchant_id = settings.PAYMENT_CREDENTIALS["click"]["merchant_id"]
            service_id = settings.PAYMENT_CREDENTIALS["click"]["merchant_service_id"]
            return_url = self.click_inapp_generate_payment_url()
            params = (
                f"?service_id={service_id}&merchant_id={merchant_id}&"
                f"amount={self.amount}&transaction_param={self.id}&"
                f"return_url={return_url}"
            )
            payment_url = f"{settings.PAYMENT_CREDENTIALS['click']['callback_url']}/{params}"

        return payment_url
