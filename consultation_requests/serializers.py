# consultation_requests/serializers.py

from rest_framework import serializers
from .models import ConsultationRequest


class ConsultationRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsultationRequest

        fields = [
            "id",
            "company_name",
            "contact_name",
            "email",
            "phone",
            "service",
            "consultant",
            "description",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate_consultant(self, value):
        if value.consultant is None:
            raise serializers.ValidationError("انتخاب مشاور الزامی است.")

        return value
