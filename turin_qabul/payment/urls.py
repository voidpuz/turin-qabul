from django.urls import path
from payment.payment_types.click.Prepare.views import ClickPrepareAPIView

urlpatterns = [
    path("click/prepare/", ClickPrepareAPIView.as_view(), name="click_prepare"),
]
