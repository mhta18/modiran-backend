from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
import logging

from .models import ConsultationRequest
from .serializers import ConsultationRequestSerializer
from .services import send_consultation_request_email

logger = logging.getLogger(__name__)


class ConsultationRequestViewSet(viewsets.ModelViewSet):

    queryset = ConsultationRequest.objects.select_related(
        "service",
        "consultant_service",
    ).all()

    serializer_class = ConsultationRequestSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["get"])
    def choices(self, request):
        return Response(
            {
                "business_industries": [
                    {"value": value, "label": label}
                    for value, label in ConsultationRequest.INDUSTRY_CHOICES
                ],
                "contact_roles": [
                    {"value": value, "label": label}
                    for value, label in ConsultationRequest.CONTACT_ROLE_CHOICES
                ],
            }
        )

    def perform_create(self, serializer):
        consultation_request = serializer.save()


       
        try:
            send_consultation_request_email(consultation_request)
        except Exception as e:
            logger.error(f"Failed to send consultation email: {e}")
