import os

from click_up import ClickUp
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

click_up = ClickUp(
    service_id=os.getenv("CLICK_SERVICE_ID"),
    merchant_id=os.getenv("CLICK_MERCHANT_ID"),
    secret_key=os.getenv("CLICK_SECRET_KEY"),
)


paylink = click_up.initializer.generate_pay_link(
    id=1, amount=settings.CLICK_AMOUNT_FIELD, return_url="https://turin.uz"
)
