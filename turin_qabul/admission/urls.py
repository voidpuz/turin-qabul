from admission.api_endpoints import AdmissionCreate
from django.urls import path

urlpatterns = [
    path("create/", AdmissionCreate.AdmissionCreateAPIView.as_view(), name="admission_create"),
]
