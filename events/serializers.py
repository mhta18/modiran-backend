from rest_framework import serializers
from .models import EventRegistration, Event

class EventSerializer(serializers.ModelSerializer):
    consultant_name = serializers.CharField(source="consultant.name", read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "consultant",
            "consultant_name",
            "price",
            "location",
            "capacity",
            "created_at",
            "date_held",
            "description",
        ]
        read_only_fields = ["id", "created_at", "consultant_name"]


class EventRegistrationSerializer(serializers.ModelSerializer):
    # event_id allows the frontend to send just the primary key
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(), source="event", write_only=True
    )

    class Meta:
        model = EventRegistration
        fields = [
            "id",
            "event_id",
            "company_name",
            "contact_name",
            "email",
            "phone",
            "business_industry",
            "contact_role",
            "created_at",
        ]
