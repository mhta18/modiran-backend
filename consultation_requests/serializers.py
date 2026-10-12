# consultation_requests/serializers.py

from rest_framework import serializers
from .models import ConsultationRequest


from rest_framework import serializers

from .models import ConsultationRequest


class ConsultationRequestSerializer(serializers.ModelSerializer):
    consultant_name = serializers.CharField(
        source="consultant_service.consultant.name", read_only=True
    )

    service_title = serializers.SerializerMethodField()

    industry_title = serializers.SerializerMethodField()
    role_title = serializers.SerializerMethodField()

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
            "service",
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

        extra_kwargs = {
            "service": {"required": False, "allow_null": True},
            "consultant_service": {"required": False, "allow_null": True},
        }

    def get_industry_title(self, obj):
        return obj.get_business_industry_display()

    def get_role_title(self, obj):
        return obj.get_contact_role_display()

    def get_service_title(self, obj):
        if obj.consultant_service and obj.consultant_service.service:
            return obj.consultant_service.service.title
        if obj.service:
            return obj.service.title
        return None

    def validate(self, data):
        service = data.get('service')
        consultant_service = data.get('consultant_service')

        # Enforce that at least one selection is made
        if not service and not consultant_service:
            raise serializers.ValidationError(
                {"non_field_errors": "لطفاً یا یک خدمت عمومی انتخاب کنید یا یک خدمت مرتبط با مشاور."}
            )

        return data
