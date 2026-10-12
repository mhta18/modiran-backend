from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related("consultant").all()
    serializer_class = EventSerializer
