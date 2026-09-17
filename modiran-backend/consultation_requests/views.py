from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import ConsultationRequest
from .serializers import ConsultationRequestSerializer
from .services import send_consultation_request_email


class ConsultationRequestViewSet(viewsets.ModelViewSet):

    queryset = ConsultationRequest.objects.select_related(
        "service",
        "consultant",
    ).all()

    serializer_class = ConsultationRequestSerializer
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

    permission_classes = [AllowAny]

    def perform_create(self, serializer):

        consultation_request = serializer.save()

        send_consultation_request_email(consultation_request)
