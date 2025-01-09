from pay.click.paylink import paylink
from rest_framework import generics
from rest_framework.response import Response


class TestAPIView(generics.GenericAPIView):
    def get(self, request):
        return Response({"message": paylink})
