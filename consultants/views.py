from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Consultant,
    Certification,
    ConsultantAvailability,
    ConsultantService,
    ConsultantVideo,
)

from .serializers import (
    ConsultantSerializer,
    CertificationSerializer,
    ConsultantServiceSerializer,
    ConsultantAvailabilitySerializer,
    ConsultantVideoSerializer,
)

class ConsultantViewSet(viewsets.ModelViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    
    @action(
        detail=True,
        methods=["get","post"],
        url_path="services"
    )

    def services(self, request, pk=None):

        consultant = self.get_object()

        consultant_services = ConsultantService.objects.filter(
            consultant=consultant
        ).select_related("service")

        serializer = ConsultantServiceSerializer(
            consultant_services,
            many=True
        )

        return Response(serializer.data)
    filterset_fields = {
        "name": ["icontains"],
        "experience_years": ["gte", "lte"],
    }

    search_fields = [
        "name",
    ]

    ordering_fields = [
        "name",
        "experience_years",
        "projects_count",
        "created_at",
    ]


class CertificationViewSet(viewsets.ModelViewSet):

    queryset = Certification.objects.select_related("consultant").all()

    serializer_class = CertificationSerializer


class ConsultantVideoViewSet(viewsets.ModelViewSet):

    queryset = ConsultantVideo.objects.select_related("consultant").all()

    serializer_class = ConsultantVideoSerializer


class ConsultantAvailabilityViewSet(viewsets.ModelViewSet):

    queryset = ConsultantAvailability.objects.select_related("consultant").all()

    serializer_class = ConsultantAvailabilitySerializer


class ConsultantServiceViewSet(viewsets.ModelViewSet):
    queryset = ConsultantService.objects.select_related("consultant", "service").all()
    serializer_class = ConsultantServiceSerializer
