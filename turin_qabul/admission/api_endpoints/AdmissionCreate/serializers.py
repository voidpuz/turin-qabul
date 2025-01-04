from admission.models import Admission
from rest_framework import serializers


class AdmissionCreateSerializer(serializers.ModelSerializer):
    passport = serializers.FileField(required=True)
    language_certificate = serializers.FileField(required=False)
    sat_certificate = serializers.FileField(required=False)
    photo = serializers.ImageField(required=True)

    class Meta:
        model = Admission
        fields = (
            "first_name",
            "last_name",
            "gender",
            "birth_date",
            "country_of_birth",
            "nationality",
            "phone_number",
            "school_name",
            "english_certificate",
            "english_certificate_score",
            "sat_score",
            "program",
            "passport",
            "language_certificate",
            "sat_certificate",
            "photo",
        )
