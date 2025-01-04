from admission.api_endpoints.AdmissionCreate.serializers import AdmissionCreateSerializer
from admission.models import Admission
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser


@extend_schema(
    summary="Create a new admission",
    description="This endpoint allows creating a new admission. Files must be uploaded using multipart/form-data.",
    request=AdmissionCreateSerializer,  # Specify the serializer
    responses={
        201: AdmissionCreateSerializer,  # Successful creation
        400: OpenApiExample(
            "Validation Error",
            summary="Validation Error Example",
            description="Example response for invalid input data.",
            value={"error": "Invalid data provided."},
        ),
    },
    examples=[
        OpenApiExample(
            name="Valid Admission Example",
            value={
                "first_name": "John",
                "surname": "Doe",
                "gender": "Male",
                "birth_date": "2000-01-01",
                "country_of_birth": 1,
                "nationality": 1,
                "mobile_phone": "+998901234567",
                "school_name": "High School XYZ",
                "english_certificate": "IELTS",
                "english_certificate_score": "7.5",
                "sat_score": "1400",
                "program_degree": "Engineering",
                "passport": "<uploaded_file>",
                "language_certificate": "<uploaded_file>",
                "sat_certificate": "<uploaded_file>",
                "photo": "<uploaded_file>",
            },
        )
    ],
)
class AdmissionCreateAPIView(CreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionCreateSerializer
    parser_classes = (MultiPartParser,)
