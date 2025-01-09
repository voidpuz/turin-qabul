from click_up import exceptions
from click_up.typing.request import ClickShopApiRequest
from click_up.views import ClickWebhook
from django.conf import settings
from django.utils.module_loading import import_string

AccountModel = import_string(settings.CLICK_ACCOUNT_MODEL)


class ClickWebhookAPIView(ClickWebhook):
    def successfully_payment(self, params):
        """
        successfully payment method process you can ovveride it
        """

        print(f"payment successful params: {params}")

    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        print(f"payment cancelled params: {params}")

    # Override check amount logic
    def check_amount(self, account: AccountModel, params: ClickShopApiRequest):  # type: ignore # noqa
        """
        check if amount is valid
        """
        received_amount = float(params.amount)
        expected_amount = float(getattr(account, settings.CLICK_AMOUNT_FIELD))

        if received_amount - expected_amount > 0.01:
            raise exceptions.IncorrectAmount("Incorrect parameter amount")
