from rest_framework import viewsets
from rest_framework import generics
from .models import Event,EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer
from .services import send_event_registration_email

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related("consultant").all()
    serializer_class = EventSerializer


class EventRegistrationCreateView(generics.CreateAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer

    def perform_create(self, serializer):
        registration = serializer.save()
        try:
            send_event_registration_email(registration)
        except Exception as e:
            # Log error without failing the HTTP request
            print(f"Error sending email: {e}")
