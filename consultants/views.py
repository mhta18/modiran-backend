from rest_framework import viewsets
from .models import (
    Consultant,
    Certification,
    ConsultantVideo,
)

from .serializers import (
    ConsultantSerializer,
    CertificationSerializer,
    ConsultantVideoSerializer,
)

class ConsultantViewSet(viewsets.ModelViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    filterset_fields = {
        "title":["icontains"],
    }

    search_fields = [
        "name",
        "title",
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
