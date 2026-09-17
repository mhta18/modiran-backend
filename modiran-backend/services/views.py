from rest_framework import viewsets
from .models import ServiceCategory
from .serializers import ServiceCategorySerializer


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
