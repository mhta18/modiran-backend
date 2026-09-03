# consultation_requests/serializers.py

from rest_framework import serializers
from .models import ConsultationRequest


from rest_framework import serializers

from .models import ConsultationRequest


class ConsultationRequestSerializer(serializers.ModelSerializer):

    consultant_name = serializers.CharField(
        source="consultant_service.consultant.name", read_only=True
    )

    service_title = serializers.CharField(
        source="consultant_service.service.title", read_only=True
    )

    industry_title = serializers.CharField(
        source="business_industry.title", read_only=True
    )

    role_title = serializers.CharField(source="contact_role.title", read_only=True)

    class Meta:
        model = ConsultationRequest

        fields = [
            "id",
            "company_name",
            "contact_name",
            "email",
            "phone",
            "business_industry",
            "industry_title",
            "contact_role",
            "role_title",
            "consultant_service",
            "consultant_name",
            "service_title",
            "description",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "consultant_name",
            "service_title",
            "industry_title",
            "role_title",
            "created_at",
        ]


from rest_framework import serializers

from .models import ContactRole


class ContactRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactRole
        fields = [
            "id",
            "title",
        ]
