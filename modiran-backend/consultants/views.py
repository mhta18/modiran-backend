from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
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

    def get_queryset(self):
        queryset = super().get_queryset()

        service_ids = self.request.query_params.getlist("service")

        if service_ids:
            queryset = queryset.filter(
                consultant_services__service_id__in=service_ids
            ).distinct()

        return queryset

    @action(detail=True, methods=["get"], url_path="services")
    def services(self, request, pk=None):
        consultant = self.get_object()

        consultant_services = ConsultantService.objects.filter(
            consultant=consultant
        ).select_related("service")

        serializer = ConsultantServiceSerializer(consultant_services, many=True)

        return Response(serializer.data)


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
