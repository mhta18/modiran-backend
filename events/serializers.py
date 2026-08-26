from rest_framework import serializers
from .models import Event
from consultants.models import Consultant


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
