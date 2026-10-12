from rest_framework import viewsets
from .models import Department, Course
from .serializers import DepartmentSerializer, CourseSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = "key"  # Allows fetching by key e.g., /api/departments/management/


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(is_active=True).order_by("-created_at")
