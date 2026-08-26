from rest_framework import serializers
from .models import (
    Consultant,
    Certification,
    ConsultantVideo,
    ConsultantAvailability,
)

class CertificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certification

        fields = [
            "id",
            "consultant",
            "title",
            "issuer",
            "certificate_number",
            "issue_date",
            "expiration_date",
            "document_url",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]


class ConsultantSerializer(serializers.ModelSerializer):

    certifications = CertificationSerializer(many=True, read_only=True)

    class Meta:
        model = Consultant

        fields = [
            "id",
            "name",
            "title",
            "email",
            "bio",
            "experience_years",
            "image_url",
            "is_verified",
            "response_time",
            "projects_count",
            "companies_count",
            "certifications",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class ConsultantVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsultantVideo

        fields = [
            "id",
            "consultant",
            "title",
            "description",
            "video_url",
            "thumbnail_url",
            "published_at",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]


class ConsultantAvailabilitySerializer(serializers.ModelSerializer):

    day_name = serializers.CharField(source="get_day_of_week_display", read_only=True)

    class Meta:
        model = ConsultantAvailability

        fields = [
            "id",
            "consultant",
            "day_of_week",
            "day_name",
            "start_time",
            "end_time",
            "is_available",
        ]

        read_only_fields = [
            "id",
            "day_name",
        ]
