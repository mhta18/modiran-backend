from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import ConsultationRequest
from .serializers import ConsultationRequestSerializer
from .services import send_consultation_request_email


class ConsultationRequestViewSet(viewsets.ModelViewSet):

    queryset = ConsultationRequest.objects.select_related(
        "service",
        "consultant",
    ).all()

    serializer_class = ConsultationRequestSerializer

    permission_classes = [AllowAny]

    def perform_create(self, serializer):

        consultation_request = serializer.save()

        send_consultation_request_email(consultation_request)

